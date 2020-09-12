# /src/views/CrawlerView

import os
import datetime as dt
from datetime import timedelta

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

    # crawl data
    rss_data_list = crawl_data()

    # get entry handler
    handler = EntryHandler()

    # create connection to graphQL api
    db_con = GraphQLConnector(api_url=api_url)

    # get all existent entries that has been updated within the last 24h
    existing_entries = db_con.get_all_entries(updated_at_gte=(dt.datetime.now() - timedelta(hours=24)))

    # check if they new crawled data contains intersecting items,
    # if yes remove them from the newly crawled data and update
    # the updated data of the old ones
    new_rss_data, existing_entries_4_update = handler.filter_duplicates(rss_data_list, existing_entries)

    for entry in existing_entries_4_update:
        db_con.update_entry_updated_at(entry)

    # handle languages
    detected_languages = handler.detect_lang(new_rss_data)
    existing_languages = db_con.get_all_languages()
    for language in detected_languages:
        db_con.create_language_if_not_existent(language, existing_languages)

    # handle tags
    determined_tags = handler.determine_tags(new_rss_data)
    existing_tags = db_con.get_all_tags()
    for tag in determined_tags:
        db_con.create_tag_if_not_existent(tag, existing_tags)

    updated_languages = db_con.get_all_languages()
    updated_tags = db_con.get_all_tags()
    new_entries = handler.build_new_entries(new_rss_data, updated_tags, updated_languages)

    # persist new entries
    for entry in new_entries:
        db_con.create_entry(entry)

    return custom_response("Crawled and persisted rss feed data!", 200)


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
