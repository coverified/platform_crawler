# /src/views/CrawlerView

import os
import datetime as dt
from datetime import timedelta

from typing import List, Dict

from src.app import log

from ..crawler.EntryHandler import EntryHandler
from ..crawler.RssCrawler import crawl_data

from flask import Blueprint, json, Response

from ..db.GraphQLConnector import GraphQLConnector

crawler_api = Blueprint('crawler_api', __name__)

# crawler api uuid token
crawler_token = os.getenv('CRAWLER_TOKEN')
api_url = os.getenv('GRAPHQL_API')


@crawler_api.route('/run/<uuid>', methods=['POST'])
def execute_crawler(uuid):
    if uuid != crawler_token:
        return custom_response("Invalid access token provided!", 400)

    if not (api_url):
        return custom_response("API url not provided. Cannot crawl and persist data!", 400)

    # get entry handler
    handler = EntryHandler()

    # create connection to graphQL api
    db_con = GraphQLConnector(api_url=api_url)

    # get all data sources
    log.info("Try to get sources for new entities ...")
    sources = db_con.get_all_sources()
    log.info("Need to check " + str(len(sources)) + " sources.")

    # crawl sources
    from feedparser import FeedParserDict
    rss_data_list: Dict[str, List[FeedParserDict]] = crawl_data(sources)

    # get all existent entries that has been updated within the last 24h
    log.info("Try to get existing entries with time delta 24h from " + api_url + "...")
    existing_entries = db_con.get_all_entries(updated_at_gte=(dt.datetime.now() - timedelta(hours=24)))
    log.info("Loaded existing " + str(len(existing_entries)) + " entries successfully!")

    # check if they new crawled data contains intersecting items,
    # if yes remove them from the newly crawled data and update
    # the updated data of the old ones
    log.info("Determining new rss data and data that needs to be updated...")
    new_rss_data, existing_entries_4_update = handler.filter_duplicates(rss_data_list, existing_entries)
    log.info(
        "Entities to be updated: " + str(len(existing_entries_4_update)) + "; New entities: "
        + str(len([item for sublist in list(new_rss_data.values()) for item in sublist])))

    for entry in existing_entries_4_update:
        db_con.update_entry_updated_at(entry)

    # handle languages
    log.info("Detecting languages for new entities...")
    detected_languages = handler.detect_lang(new_rss_data)
    existing_languages = db_con.get_all_languages()
    for language in detected_languages:
        db_con.create_language_if_not_existent(language, existing_languages)
    log.info("Language detection complete.")

    # handle tags
    log.info("Determining tags for new entities...")
    determined_tags = handler.determine_tags(new_rss_data)
    existing_tags = db_con.get_all_tags()
    for tag in determined_tags:
        db_con.create_tag_if_not_existent(tag, existing_tags)
    log.info("Tag determination complete.")

    log.info("Build and persist new entities...")
    updated_languages = db_con.get_all_languages()
    updated_tags = db_con.get_all_tags()
    new_entries = handler.build_new_entries(new_rss_data, updated_tags, updated_languages, sources)

    # persist new entries
    for entry_set in new_entries:
        for entry in entry_set:
            db_con.create_entry(entry)

    log.info("Crawled and persisted " + str(
        len([item for sublist in new_entries for item in sublist])) + " rss feed elements!")
    return custom_response("Crawled and persisted " + str(len(new_entries)) + " rss feed elements!", 200)


def custom_response(res, status_code):
    """
    Convert the resulting data to a custom response including header data
    :param res: the response to be processed
    :param status_code: the status code
    :return: transformed custom response data
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
