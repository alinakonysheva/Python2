# 3. Задание на закрепление знаний по модулю yaml.
# Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
# Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
# второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
# отсутствующим в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
# а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import yaml

data_in = {'items': ['dress', 'shoes', 'skirt', 'jeans'], 'quantity': 4,
           'price': {'dress': '100€',  'shoes': '50€', 'skirt': '40€', 'jeans': '25€'}}

with open('file.yaml', 'w', encoding='utf-8') as file_in:
    yaml.dump(data_in, file_in, default_flow_style=False, allow_unicode=True)

with open("file.yaml", 'r', encoding='utf-8') as file_out:
    data_out = yaml.load(file_out, Loader=yaml.FullLoader)

for row1 in data_in:
    for i, row2 in enumerate(data_out):
        if row1 == row2:
            print(f'{i} string is correct!')

