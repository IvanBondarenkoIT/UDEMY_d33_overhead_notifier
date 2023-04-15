import requests


class JsonManage:
    def __init__(self, url_to_get_json):
        self.__url_to_get_json = url_to_get_json

    def get_json(self) -> tuple:
        response = requests.get(url=self.__url_to_get_json)
        response.raise_for_status()
        return response.json()

