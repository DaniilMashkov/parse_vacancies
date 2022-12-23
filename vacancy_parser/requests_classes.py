from abc import ABC, abstractmethod
import requests
from vacancy_parser.connector import Connector


class Engine(ABC):
    @abstractmethod
    def get_request(self, text: str):
        pass

    @staticmethod
    def get_connector(file_name: str) -> object:
        return Connector(file_name)


class HH(Engine):
    """Записывает полученные от API данные в json"""

    def get_request(self, text: str) -> None:
        hh_responses = []

        for page in range(10):
            print('Выполняется запрос...')

            url = f'https://api.hh.ru/vacancies?{page=}&per_page=100&{text=}'
            response = requests.request("GET", url)
            if response.status_code > 301:
                break
            else:
                hh_responses.extend(response.json().get('items'))

        con_obj = HH.get_connector('data/hh_responses.json')
        con_obj.insert(hh_responses)


class SuperJob(Engine):
    """Записывает полученные от API данные в json"""

    def get_request(self, keyword: str) -> None:
        sj_responses = []
        headers = {
            'X-Api-App-Id':
                'v3.r.120558577.03d5d61129ce8b416a420a9c0c3a8d89005f9067.f69f0541855923e9f201e077ed4f7dc57edd7e5c',
            'Host': 'api.superjob.ru'}

        for page in range(1, 6):
            print('Выполняется запрос...')
            url = f'https://api.superjob.ru/2.0/vacancies/?{page=}&count=100&{keyword=}'
            response = requests.request("GET", url, headers=headers)
            if response.status_code > 301:
                break
            else:
                sj_responses.extend(response.json().get('objects'))

        con_obj = SuperJob.get_connector('data/sj_responses.json')
        con_obj.insert(sj_responses)
