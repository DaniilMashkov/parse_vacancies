import re


class Vacancy:
    __slots__ = ('vacancy_name', 'link', 'description', 'salary')

    def __init__(self, pattern: dict):
        self.vacancy_name = pattern.get('name')
        self.link = pattern.get('link')
        self.description = pattern.get('description') or ''
        self.salary = pattern.get('salary') if pattern.get('salary') \
            else {'from': 0, 'to': 0, 'currency': 'RUR'}

    def get_parsed_dict(self) -> dict:
        return {
            'name': self.vacancy_name,
            'link': self.link,
            'description': self.parse_description(),
            'salary': self.parse_salary()
        }

    def __gt__(self, other: int) -> bool:
        return (self.salary.get('from') or 0) > (other or 0)

    def __lt__(self, other: int) -> bool:
        return (self.salary.get('from') or 0) < (other or 0)

    def __eq__(self, other: int) -> bool:
        return (self.salary.get('from') or 0) == (other or 0)

    def __ge__(self, other: int) -> bool:
        return (self.salary.get('from') or 0) >= (other or 0)

    def __le__(self, other: int) -> bool:
        return (self.salary.get('from') or 0) <= (other or 0)

    def parse_salary(self):
        if self.salary:
            return f"{self.salary['from']} - {self.salary['to']} ({(self.salary.get('currency') or 'RUR')})"

    def parse_description(self) -> str:
        if isinstance(self.description, dict):
            return re.sub(r'<.*?>|&.*?;', '',
                          (self.description.get('responsibility') or self.description.get('requirement')) or '')
        else:
            return re.sub(r'<.*?>|&.*?;|\\n\\xa0', '', str(self.description)).replace(';', '\n')

    def __repr__(self) -> str:
        return f'\n{self.vacancy_name}\n{self.link}\n{"-" * 30}\
                \n{self.parse_description()}\n{"-" * 30}\nЗП: {self.parse_salary()}\n{"#" * 50}\n'


class CountMixin:
    counter = 0

    @property
    def get_count_of_vacancy(self) -> int:
        return CountMixin.counter

    @get_count_of_vacancy.setter
    def get_count_of_vacancy(self, value: int) -> None:
        CountMixin.counter = value


class HHVacancy(Vacancy, CountMixin):  # add counter mixin
    """ HeadHunter Vacancy """

    def __init__(self, data: dict) -> None:
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

    def __init__(self, data: dict) -> None:
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
