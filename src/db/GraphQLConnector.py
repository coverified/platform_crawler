# /src/schema/GraphQLConnector

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from src.db.coverified_schema import coverified_schema as schema, LanguageCreateInput, TagCreateInput, \
    EntryWhereInput, EntryUpdateInput
from src.app import log


class GraphQLConnector:
    http_endpoint = None

    def __init__(self, api_url):
        self.http_endpoint = HTTPEndpoint(url=api_url)

    def get_all_languages(self):
        query = self.__get_query()
        query.all_languages()
        log.debug(query)
        data = self.http_endpoint(query)
        return (query + data).all_languages

    def create_language(self, lang_name):
        mutation = self.__get_mutation()
        mutation.create_language(data=LanguageCreateInput(name=lang_name))
        log.debug(mutation)
        self.http_endpoint(mutation)

    def create_language_if_not_existent(self, lang_name, all_existing_languages=None):
        # get all existing languages first if they are not provided
        if not all_existing_languages:
            all_existing_languages = self.get_all_languages()

        # if language is not present in db, create it
        if not (next((x for x in all_existing_languages if x.name == lang_name), None)):
            self.create_language(lang_name)
            log.debug("Created new language entry: " + lang_name)
        else:
            log.debug("Language " + lang_name + " already exist. No need to add a new entry.")

    def get_all_tags(self):
        query = self.__get_query()
        query.all_tags()
        log.debug(query)
        data = self.http_endpoint(query)
        return (query + data).all_tags

    def create_tag(self, tag_name):
        mutation = self.__get_mutation()
        mutation.create_tag(data=TagCreateInput(name=tag_name))
        log.debug(mutation)
        self.http_endpoint(mutation)

    def create_tag_if_not_existent(self, tag_name, all_existing_tags=None):
        # get all existing tags first if they are not provided
        if not all_existing_tags:
            all_existing_tags = self.get_all_tags()

        # if tag is not present in db, create it
        if not (next((x for x in all_existing_tags if x.name == tag_name), None)):
            self.create_language(tag_name)
            log.debug("Created new tag entry: " + tag_name)
        else:
            log.debug("Tag " + tag_name + " already exist. No need to add a new entry.")

    def update_entry_updated_at(self, entry):
        mutation = self.__get_mutation()
        # to just update the updated_at field, set the same title again
        mutation.update_entry(id=entry.id, data=EntryUpdateInput(title=entry.title))
        log.debug(mutation)
        self.http_endpoint(mutation)

    def get_all_entries(self, updated_at_gte=None):
        query = self.__get_query()
        query.all_entries(where=EntryWhereInput(updated_at_gte=updated_at_gte))
        log.debug(query)
        data = self.http_endpoint(query)
        return (query + data).all_entries

    def create_entry(self, entry_input_data):
        mutation = self.__get_mutation()
        mutation.create_entry(data=entry_input_data)
        self.http_endpoint(mutation)

    @staticmethod
    def __get_mutation():
        return Operation(schema.Mutation)

    @staticmethod
    def __get_query():
        return Operation(schema.Query)
