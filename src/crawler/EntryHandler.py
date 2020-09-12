from src.app import log

from dateutil.parser import parse

# language detection imports
from langdetect import detect
from langdetect import DetectorFactory

from src.db.coverified_schema import EntryCreateInput, LanguageRelateToOneInput, LanguageWhereUniqueInput
from src.util.StringUtil import StringUtil

DetectorFactory.seed = 0  # enforce consistent language detection results


class EntryHandler:

    def filter_duplicates(self, rss_data_list, existing_entries):
        # map title + published date + content + url to a string and compare them
        rss_data_strings = {StringUtil.clean_string(entry.title) +
                            str(parse(entry.published).date()) +
                            StringUtil.clean_string(entry.summary) +
                            entry.link: entry
                            for entry in rss_data_list}
        existing_entries_strings = {
            entry.title +
            entry.publish_date +
            entry.content +
            entry.url: entry
            for entry in existing_entries
        }

        # unique new rss data
        new_rss_data = set()
        for key in rss_data_strings.keys():
            if not (existing_entries_strings.__contains__(key)):
                new_rss_data.add(rss_data_strings.get(key))

        # existing entries that needs to be updated
        entries_4_update = set()
        for key in existing_entries_strings.keys():
            if rss_data_strings.__contains__(key):
                entries_4_update.add(existing_entries_strings.get(key))

        return new_rss_data, entries_4_update

    def build_new_entries(self, rss_data_list, all_tags, all_languages):
        language_map = self.__map_to_name(all_languages)
        tag_map = self.__map_to_name(all_tags)

        new_entries = set()
        for feed_entry in rss_data_list:
            # get tags

            # get language
            language_id = language_map.get(self.__detect_entry_lang(feed_entry)).id
            language = LanguageRelateToOneInput(connect=LanguageWhereUniqueInput(id=language_id))

            new_entries.add(EntryCreateInput(publish_date=str(parse(feed_entry.published).date()),
                                             title=StringUtil.clean_string(feed_entry.title),
                                             content=StringUtil.clean_string(feed_entry.summary),
                                             url=feed_entry.link,
                                             language=language,
                                             ))
            # todo JH tags
        return new_entries

    def detect_lang(self, rss_data_list):
        languages = set(map(lambda feed_entry: self.__detect_entry_lang(feed_entry), rss_data_list))
        log.debug("Detected languages: " + ", ".join(languages))
        return languages

    @staticmethod
    def __detect_entry_lang(feed_entry):
        return detect(StringUtil.clean_string(feed_entry.title) + StringUtil.clean_string(feed_entry.summary))

    @staticmethod
    def determine_tags(rss_data_list):
        # todo JH
        return set()

    @staticmethod
    def __map_to_name(lst):
        res_dct = {i.name: i for i in lst}
        return res_dct
