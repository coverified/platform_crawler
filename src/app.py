# src/app.py
import json

import logging as log

from flask import Flask

from .config import app_config
from .crawler.RssCrawler import create_crawler

# import feed_api blueprint
from .views.CrawlerView import crawler_api as crawler_blueprint

# api limiter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import configparser


def create_app(env_name):
    """
    Create app
    """

    # app initialization
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    # defaults
    log_level = log.INFO

    # read config
    config = configparser.ConfigParser()
    config.read('cfg/config.cfg')

    # debug
    if app_config[env_name].DEBUG:
        log_level = log.DEBUG  # debug log enabled

    # configure logger
    log.basicConfig(format='[%(asctime)s] [%(module)s] [%(levelname)s] [%(funcName)s] %(message)s',
                    datefmt='%Y-%m-%d,%H:%M:%S:%f', level=log_level)

    # register the feed api blueprint
    app.register_blueprint(crawler_blueprint, url_prefix='/api/v1/crawler')

    # start the crawler
    keywords = json.loads(config.get("crawler", "keywords"))
    create_crawler(keywords)

    # limit the number of api calls
    Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["20000 per day", "500 per hour"]
    )

    @app.route('/', methods=['GET'])
    def index():
        """
        main endpoint -> cite Admiral Ackbar
        """
        return '“It’s a trap!” – Admiral Ackbar, Return of the Jedi'

    return app
