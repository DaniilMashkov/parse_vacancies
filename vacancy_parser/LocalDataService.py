from connector import Connector
from parse_data_classes import HHVacancy, SJVacancy


class LocalDataService:

    def __init__(self, file_path: str) -> None:
        con_obj = Connector(file_path)
        self.data = con_obj.eject()
        self.lst = []

    def collect(self, service: type) -> list[HHVacancy | SJVacancy]:
        for item in self.data:
            inst = service(item)
            self.lst.append(inst)
        return self.lst

    def sort_data(self, flag=False) -> None:
        self.lst.sort(reverse=flag)

    def filter_data(self, min_salary: int) -> list:
        return list(filter(lambda x: (x.salary.get('from') or 0) >= min_salary, self.lst))
