from connector import Connector
import re


class Vacancy:
    __slots__ = ('vacancy_name', 'link', 'description', 'salary')

    def __init__(self, pattern: dict):
        self.vacancy_name = pattern.get('name')
        self.link = pattern.get('link')
        self.description = pattern.get('description'), None
        self.salary = pattern.get('salary'), None

    def parse_salary(self):
        if self.salary[0]:
            try:
                return f"{self.salary[0]['from']} - {self.salary[0]['to']} ({self.salary[0]['currency']})"
            except KeyError:
                return f"{self.salary[0]['from']} - {self.salary[0]['to']}"

    def parse_description(self):
        if self.description[0]:
            try:
                return f"{re.sub(r'<.*?>|&.*?;', ' ', self.description[0]['requirement'])}\
                \n{re.sub(r'<.*?>|&.*?;', ' ', self.description[0]['responsibility'])}"
            except:
                return re.sub(r'<.*?>|&.*?;|\\n\\xa0', '', str(self.description[0])).replace(';', '\n')

    def __repr__(self):
        return f'{"*" * 30}\n{self.vacancy_name}\n{self.link}\n{"-" * 30}\
                \n{self.parse_description()}\n{"-" * 30}\nЗП: {self.parse_salary()}'


class CountMixin:
    counter = 0

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        return CountMixin.counter

    @get_count_of_vacancy.setter
    def get_count_of_vacancy(self, value):
        CountMixin.counter += value


class HHVacancy(Vacancy, CountMixin):  # add counter mixin
    """ HeadHunter Vacancy """

    def __init__(self, data):
        self.get_count_of_vacancy += 1
        print(self.get_count_of_vacancy)
        self.file = data
        args = {
            'name': self.file.get('name'),
            'link': self.file.get('alternate_url'),
            'description': self.file.get('snippet'),
            'salary': self.file.get('salary')
        }
        super().__init__(args)



class SJVacancy(Vacancy, CountMixin):
    """ SuperJob Vacancy """

    def __init__(self, data):
        self.file = data
        args = {
            'name': self.file.get('profession'),
            'link': self.file.get('link'),
            'description': self.file.get('vacancyRichText'),
            'salary':
                {'from': self.file.get('payment_from'),
                 'to': self.file.get('payment_to')}
        }
        super().__init__(args)


con_obj = Connector('../data/hh_responses.json')
file = con_obj.eject()
for item in file:
    hh = HHVacancy(item)

    print(hh)

# con_obj = Connector('../data/sj_responses.json')
# file = con_obj.eject()
# for item in file:
#     hh = SJVacancy(item)
#     print(hh)
