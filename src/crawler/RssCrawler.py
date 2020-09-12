# /src/views/CrawlerView

import feedparser

from src.app import log
from src.util.StringUtil import StringUtil

keywords = []
feeds = []


def create_crawler(filter_words, feed_urls):
    log.info("Configure rss crawler...")
    # set the global vals
    global keywords
    keywords = filter_words

    global feeds
    feeds = feed_urls

    log.info("Successfully configured rss crawler!")


def crawl_data():
    log.info("Collecting data from rss feeds...")
    rss_data_list = crawl_rss_data()
    log.info("Collected " + str(len(rss_data_list)) + " elements.")
    return rss_data_list


def crawl_rss_data():
    return list(filter(lambda x: filter_keywords(StringUtil.clean_string(StringUtil.filter_html(x.title + x.summary))),
                       flatten([feedparser.parse(feed_url).entries for feed_url in feeds])))


def filter_keywords(string):
    return bool(any(x in string.casefold() for x in keywords))


def flatten(list):
    flat_list = []
    for sublist in list:
        for item in sublist:
            flat_list.append(item)
    return flat_list
