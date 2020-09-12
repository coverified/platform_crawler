# /src/schema/GraphQLConnector

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from src.db.coverified_schema import coverified_schema as schema, LanguageCreateInput, TagCreateInput
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

    def get_all_tags(self):
        query = self.__get_query()
        query.all_tags()
        log.debug(query)
        data = self.http_endpoint(query)
        return (query + data).all_tags

    def create_tag(self, id):
        mutation = self.__get_mutation()
        mutation.create_tag(data=TagCreateInput(name=id))
        log.debug(mutation)
        self.http_endpoint(mutation)

    def create_language(self, id):
        mutation = self.__get_mutation()
        mutation.create_language(data=LanguageCreateInput(name=id))
        log.debug(mutation)
        self.http_endpoint(mutation)

    @staticmethod
    def __get_mutation():
        return Operation(schema.Mutation)

    @staticmethod
    def __get_query():
        return Operation(schema.Query)
