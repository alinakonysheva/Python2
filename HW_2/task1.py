
# 1. Задание на закрепление знаний по модулю CSV.
# Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и
#  формирующий новый «отчетный» файл в формате CSV. Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
# их открытие и считывание данных.
# В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
#  «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
#  Значения каждого параметра поместить в соответствующий список.
#  Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
#  В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него
# названия столбцов отчета в виде списка:
#  «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
#  Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных
# в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import csv
import re

# Посмотрим на файлы, оценим что надо искать, и подберем кодировку, подумаем про regexp:
'''
with open('info_1.txt', encoding='windows-1251') as file_:
    for string in file_:
        print(string)
        '''


def get_data():
    # заводим списки подо все что будем собирать из текстовых файлов
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []
    # Определимся с заголовками:
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)
    # Перебираем файлы, записываем информацию в столбики:
    for i in range(1, 4):
        file_name = 'info_%s.txt' % i
        content = open(file_name, encoding='windows-1251')
        data = content.read()

        # Получаем список изготовителей системы
        os_prod_all = re.findall(r'Изготовитель системы:\s*\S*', data)
        os_prod_list.append(os_prod_all[0].split()[2])

        # Получаем список названий ОС
        os_name_all = re.findall(r'Windows\s\S*', data)
        os_name_list.append(os_name_all[0])

        # Получаем список кодов продукта
        os_code_all = re.findall(r'Код продукта:\s*\S*', data)
        os_code_list.append(os_code_all[0].split()[2])

        # Получаем список типов системы
        os_type_all = re.findall(r'Тип системы:\s*\S*', data)
        os_type_list.append(os_type_all[0].split()[2])

    for i in range(0, 3):
        row = [os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]]
        main_data.append(row)

    return main_data


def write_to_csv(file):
    main_data = get_data()
    with open(file, 'w') as file:
        writer = csv.writer(file)
        for row in main_data:
            writer.writerow(row)


file_final = 'information.csv'
write_to_csv(file_final)