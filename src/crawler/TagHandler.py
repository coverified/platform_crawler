import os
import json
import requests

from src.app import log

class TagHandler:
    __ibm_cloud_nlu_url__ = os.getenv('IBM_CLOUD_NLU_API_URL')
    __ibm_cloud_nlu_api_key__ = os.getenv('IBM_CLOUD_NLU_API_KEY')

    __headers__ = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

    def __init__(self, ibm_cloud_nlu_url=os.getenv('IBM_CLOUD_NLU_API_URL'),
                 ibm_cloud_nlu_api_key=os.getenv('IBM_CLOUD_NLU_API_KEY')):
        self.__ibm_cloud_nlu_url__ = ibm_cloud_nlu_url
        self.__ibm_cloud_nlu_api_key__ = ibm_cloud_nlu_api_key

        if not self.__ibm_cloud_nlu_url__ or not self.__ibm_cloud_nlu_api_key__:
            log.error("Missing configuration parameters for 'IBM_CLOUD_NLU_API_URL' and/or 'IBM_CLOUD_NLU_API_KEY'")
            raise EnvironmentError(
                "Missing configuration parameters for 'IBM_CLOUD_NLU_API_URL' and/or 'IBM_CLOUD_NLU_API_KEY'")

    def get_tags_from(self, string):
        categories = self.__get_categories(string)

        if bool(categories):
            return set(map(lambda category: category['label'].strip("/"), categories))
        else:
            return None

    def __get_categories(self, string):
        cleaned_string = string.replace("\"", "").replace("“", " ")
        payload = """{
            "text": \"""" + cleaned_string + """\",
            "features": {
                "categories":{}
            }
        }
        """

        req_res = requests.post(url=self.__ibm_cloud_nlu_url__, data=payload.encode('utf-8'), headers=self.__headers__,
                                auth=('apikey', self.__ibm_cloud_nlu_api_key__)).content

        # try to get categories
        try:
            return json.loads(req_res)['categories']
        except KeyError:
            return None
