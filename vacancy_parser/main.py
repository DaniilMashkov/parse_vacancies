from vacancy_parser.utils import get_remote_data, get_local_data


def main() -> None:
    while True:
        sel_category = input('Выберете действие:'
                             '\n1.Запросить данные с ресурса\n2.Получить локальные данные\
                             \nЛюбой другой символ для выхода\n')
        if sel_category == '1':
            get_remote_data()
        if sel_category == '2':
            get_local_data()
        else:
            exit()


if __name__ == '__main__':
    main()
