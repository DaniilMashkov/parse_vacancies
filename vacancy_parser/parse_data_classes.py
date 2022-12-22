import re


class Vacancy:
    __slots__ = ('vacancy_name', 'link', 'description', 'salary')

    def __init__(self, pattern: dict):
        self.vacancy_name = pattern.get('name')
        self.link = pattern.get('link')
        self.description = pattern.get('description') or None
        self.salary = pattern.get('salary') or {'from': 0, 'to': 0}

    def __gt__(self, other):
        result = self.salary.get('from', 0) > other.salary.get('from', 0)
        return result

    def __lt__(self, other):
        result = self.salary.get('from', 0) < other.salary.get('from', 0)
        return result

    def __eq__(self, other):
        result = self.salary.get('from', 0) == other.salary.get('from', 0)
        return result

    def parse_salary(self):
        if self.salary:
            try:
                return f"{self.salary['from']} - {self.salary['to']} ({self.salary['currency']})"
            except KeyError:
                return f"{self.salary['from']} - {self.salary['to']}"

    def parse_description(self):
        if self.description:
            try:
                return f"{re.sub(r'<.*?>|&.*?;', ' ', self.description['requirement'])}\
                \n{re.sub(r'<.*?>|&.*?;', ' ', self.description['responsibility'])}"
            except:
                return re.sub(r'<.*?>|&.*?;|\\n\\xa0', '', str(self.description)).replace(';', '\n')

    def __repr__(self):
        return f'\n{self.vacancy_name}\n{self.link}\n{"-" * 30}\
                \n{self.parse_description()}\n{"-" * 30}\nЗП: {self.parse_salary()}\n{"#" * 50}\n'


class CountMixin:
    counter = 0

    @property
    def get_count_of_vacancy(self):
        return CountMixin.counter

    @get_count_of_vacancy.setter
    def get_count_of_vacancy(self, value):
        CountMixin.counter = value


class HHVacancy(Vacancy, CountMixin):  # add counter mixin
    """ HeadHunter Vacancy """

    def __init__(self, data):
        self.get_count_of_vacancy += 1
        args = {
            'name': data.get('name'),
            'link': data.get('alternate_url'),
            'description': data.get('snippet'),
            'salary': data.get('salary')
        }
        super().__init__(args)


class SJVacancy(Vacancy, CountMixin):  # add counter mixin
    """ SuperJob Vacancy """

    def __init__(self, data):
        self.get_count_of_vacancy += 1
        args = {
            'name': data.get('profession'),
            'link': data.get('link'),
            'description': data.get('vacancyRichText'),
            'salary':
                {'from': data.get('payment_from'),
                 'to': data.get('payment_to')}
        }
        super().__init__(args)
