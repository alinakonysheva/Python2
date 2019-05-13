# -- принимает сообщение клиента;
# -- формирует ответ клиенту;
# -- отправляет ответ клиенту;
# -- имеет параметры командной строки:
#       -p <port> — TCP-порт для работы (по умолчанию использует 7777);
#       -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
import sys
from HW_3.config import *
from HW_3.utils import get_message, send_message
from socket import socket, AF_INET, SOCK_STREAM


# Формируем ответ:
def presence_answer(presence_message):
    # Делаем проверки
    if ACTION in presence_message and \
            presence_message[ACTION] == PRESENCE and \
            TIME in presence_message and \
            isinstance(presence_message[TIME], float):
        # Если всё хорошо шлем ОК
        return {RESPONSE: 200}
    else:
        # Шлем код ошибки
        return {RESPONSE: 400, ERROR: 'Не верный запрос'}


if __name__ == '__main__':
    # Создается TCP-сокет сервера
    server = socket(AF_INET, SOCK_STREAM)
    # Получаем аргументы скрипта
    # ------------ip-адрес-----------#
    # если ip-адрес указан в параметрах
    try:
        addr = sys.argv[1]
    # если ip-адрес не указан в параметрах
    except IndexError:
        addr = ''
    # пробуем порт из параметров
    try:
        port = int(sys.argv[2])
    # если его в параметрах нет
    except IndexError:
        port = 7777

    # Присваивает порт 8888
    server.bind((addr, port))
    server.listen(5)
    while True:
        # принимаем запрос на соединение
        client, addr = server.accept()
        # принимаем клиентское сообщение
        presence = get_message(client)
        print(presence)
        # ответ будет
        response = presence_answer(presence)
        # отправляем ответ
        send_message(client, response)
        # закрываем соединение
        client.close()
