import lxml.html

import html


class StringUtil:

    @staticmethod
    def clean_string(string):
        # we don't want soft hyphen in the db
        soft_hyphen_html = "&#173;"
        # we don't want line breaks in the db
        return html.unescape(string.replace(soft_hyphen_html, "").replace("\n", " "))

    @staticmethod
    def filter_html(string):
        if not string:
            return string
        return lxml.html.fromstring(string).text_content()

    # @staticmethod
    # def date_from_date_time(string):
