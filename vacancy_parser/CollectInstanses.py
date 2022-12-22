from connector import Connector
from parse_data_classes import HHVacancy, SJVacancy


class Collect:

    def __init__(self, file_path: str) -> None:
        con_obj = Connector(file_path)
        self.data = con_obj.eject()
        self.lst = []

    def collect(self, service: HHVacancy | SJVacancy):
        for item in self.data:
            # print(item)
            # exit()
            inst = service(item)
            self.lst.append(inst)
        return self.lst

    def sort_data(self, flag=False):
        self.lst.sort(reverse=flag)




s = Collect('../data/hh_responses.json')
# d = Collect('../data/sj_responses.json')

s.collect(HHVacancy)

print(s.sort_data())
print(s.lst)