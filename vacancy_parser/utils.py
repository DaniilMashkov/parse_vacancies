from requests_classes import HH, SuperJob
from LocalDataService import LocalDataService
from parse_data_classes import HHVacancy, SJVacancy
from connector import Connector


def get_remote_data():
    sel_service = input('1.HH.RU\n2.SuperJob\nЛюбой символ другой символ для выбора обоих\n')
    keyword = input('Введите ключевое слово:\n')

    sj_instance = SuperJob()
    hh_instanсe = HH()

    if sel_service == '1':
        hh_instanсe.get_request(keyword)
    elif sel_service == '2':
        sj_instance.get_request(keyword)
    else:
        hh_instanсe.get_request(keyword)
        sj_instance.get_request(keyword)


def get_local_data():
    sel_service = input('1.HH.RU\n2.SuperJob\nЛюбой символ другой символ для выхода в основное меню\n')

    hh_instance = LocalDataService('../data/hh_responses.json')
    sj_instance = LocalDataService('../data/sj_responses.json')
    connector_instance = Connector('../data/result.json')

    if sel_service == '1':
        vacancies = hh_instance.collect(HHVacancy)
        print(f'\nНайдено {vacancies[0].get_count_of_vacancy} вакансий\n')

        sort(hh_instance)
        get_result(connector_instance, hh_instance.lst)

    if sel_service == '2':
        vacancies = sj_instance.collect(SJVacancy)
        print(f'\nНайдено {vacancies[0].get_count_of_vacancy} вакансий\n')

        sort(sj_instance)
        get_result(connector_instance, sj_instance.lst)


def sort(instance):
    sort_input = input('1.Сортировать по убыванию\n2.Сортировать по возрастанию\n3.Ввести нижний порог ЗП\n')
    if sort_input == '1':
        instance.sort_data()
    if sort_input == '2':
        instance.sort_data(flag=True)
    elif sort_input == '3':
        while True:
            min_salary = input('Желаемая сумма\n')
            if min_salary.isdigit():
                # instance.sort_data(True)
                instance.filter_data(int(min_salary))
                break
            else:
                print('Нужно вводить цифры')
    else:
        print('Выведутся неотсортированные данные\n')

    amount = input('Количество выводимых вакансий:\n')
    try:
        instance.lst = instance.lst[:int(amount)]
    except ValueError:
        print('Некорректный ввод, будут выведены все доступные вакансии')


def get_result(connector_instance: Connector, lst: list) -> None:
    connector_instance.insert_parsed(lst)
    print(*lst)
