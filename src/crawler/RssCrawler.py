# /src/views/CrawlerView

import feedparser
from typing import List, Dict

from src.app import log
from src.db.coverified_schema import Source
from src.util.StringUtil import StringUtil

keywords = []


def create_crawler(filter_words):
    log.info("Configure rss crawler...")
    # set the global vals
    global keywords
    keywords = filter_words
    log.info("Successfully configured rss crawler!")


def crawl_data(feed_urls: List[Source]):
    log.info("Collecting data from rss feeds...")
    rss_data_dict = crawl_rss_data(feed_urls)
    log.info("Collected " + str(len([item for sublist in list(rss_data_dict.values()) for item in sublist])) + " elements.")
    return rss_data_dict


def crawl_rss_data(feed_urls: List[Source]):
    return dict(zip(map(lambda fu: fu.id, feed_urls),
                    [list(filter(
                        lambda x: filter_keywords(StringUtil.clean_string(StringUtil.filter_html(x.title + x.summary))),
                        feedparser.parse(feed_url.url).entries)) for feed_url in feed_urls]))


def filter_keywords(string):
    return bool(any(x in string.casefold() for x in keywords))
