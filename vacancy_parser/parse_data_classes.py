class Vacancy:
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        pass

    def __repr__(self):
        pass


class HHVacancy(Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """

    pass


class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    pass


class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        pass
