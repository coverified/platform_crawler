from src.app import log

from dateutil.parser import parse
from functools import reduce

# language detection imports
from langdetect import detect
from langdetect import DetectorFactory

from src.crawler.TagHandler import TagHandler
from src.db.coverified_schema import EntryCreateInput, LanguageRelateToOneInput, LanguageWhereUniqueInput, \
    TagRelateToManyInput, TagWhereUniqueInput
from src.util.StringUtil import StringUtil

DetectorFactory.seed = 0  # enforce consistent language detection results


class EntryHandler:
    tag_handler = TagHandler()

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
            tag_ids = list()
            for tag_name in self.__determine_entry_tag(feed_entry):
                tag_id = tag_map.get(tag_name).id
                tag_ids.append(TagWhereUniqueInput(id=tag_id))

            tags = TagRelateToManyInput(connect=tag_ids)

            # get language
            language_id = language_map.get(self.__detect_entry_lang(feed_entry)).id
            language = LanguageRelateToOneInput(connect=LanguageWhereUniqueInput(id=language_id))

            new_entries.add(EntryCreateInput(publish_date=str(parse(feed_entry.published).date()),
                                             title=StringUtil.clean_string(feed_entry.title),
                                             content=StringUtil.clean_string(feed_entry.summary),
                                             url=feed_entry.link,
                                             language=language,
                                             tags=tags
                                             ))

        log.info("New entities: " + str(len(new_entries)))
        return new_entries

    def detect_lang(self, rss_data_list):
        languages = set(map(lambda feed_entry: self.__detect_entry_lang(feed_entry), rss_data_list))
        log.debug("Detected languages: " + ", ".join(languages))
        return languages

    @staticmethod
    def __detect_entry_lang(feed_entry):
        return detect(StringUtil.clean_string(feed_entry.title) + StringUtil.clean_string(feed_entry.summary))

    def determine_tags(self, rss_data_list):
        tag_list = list(map(lambda entry: self.__determine_entry_tag(entry), rss_data_list))
        if tag_list:
            tags = reduce(set.union, tag_list)
        else:
            tags = set()
        log.debug("Determined tags: " + ", ".join(tags))
        return tags

    def __determine_entry_tag(self, feed_entry):
        return self.tag_handler.get_tags_from(
            StringUtil.clean_string(feed_entry.title) + StringUtil.clean_string(feed_entry.summary))

    @staticmethod
    def __map_to_name(lst):
        res_dct = {i.name: i for i in lst}
        return res_dct
