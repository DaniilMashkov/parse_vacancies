from requests_classes import HH, SuperJob


def main():
    while True:
        sel_category = input('Выберете действие:\n1.Запросить данные с ресурса\n2.Получить локальные данные\n')
        if sel_category == '1':
            sel_service = input('1.HH.RU\n2.SuperJob\nЛюбой символ другой символ для вывода обоих\n')
            keyword = input('Введите ключевое слово:\n')

            sj_instance = SuperJob()
            hh_instanсe = HH()

            if sel_service == '1':
                hh_instanсe.get_request(keyword)
                break
            elif sel_service == '2':
                sj_instance.get_request(keyword)
                break
            else:
                hh_instanсe.get_request(keyword)
                sj_instance.get_request(keyword)
                break

        if sel_category == '2':
            sel_service = input('1.HH.RU\n2.SuperJob\nЛюбой символ другой символ для вывода обоих\n')
            amount = input('Количество выводимых вакансий:\n')
            try:
                int(amount)
                sort = input('1.Сортировать по убыванию\n2.Сортировать по возрастанию\n3.Ввести нижний порог ЗП\n')
                if sort == '1':
                    break
                if sort == '2':
                    break
                elif sort == '3':
                    while True:
                        min_salary = input('Желаемая сумма\n')
                        if min_salary.isdigit():
                            break
                        else:
                            print('Нужно вводить цифры')
                    break
                else:
                    print('Выведутся неотсортированные данные\n')
            except ValueError:
                print('Нужно вводить числа\n')

            args = (sel_service, amount, sort := None, min_salary := None)
        else:
            print('Некорректный ввод\n')


if __name__ == '__main__':
    main()
