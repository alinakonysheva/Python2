# -- сформировать presence-сообщение;
# -- отправить сообщение серверу;
# -- получить ответ сервера;
# -- разобрать сообщение сервера;
# -- параметры командной строки скрипта client.py <addr> [<port>]:
# -- addr — ip-адрес сервера;
# -- port — tcp-порт на сервере, по умолчанию 7777.

import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from HW_3.errors import UsernameToLongError, ResponseCodeLenError, MandatoryKeyError, ResponseCodeError
from HW_3.config import *
from HW_3.utils import send_message, get_message

# функция формирования сообщения
def create_presence(account_name='Guest'):
    # учтем ограничение на имя пользователя / название чата (name): 25 символов
    if len(account_name) > 25:
        # выводим ошибку в случае если имя пользователя слишком длинное
        raise UsernameToLongError(account_name)

     # Если account_name не строковая
    if not isinstance(account_name, str):
        # Генерируем ошибку
        raise TypeError
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return message

# Разбраем ответа сервера
def translate_message(response):
    # Передали не словарь
    if not isinstance(response, dict):
        raise TypeError
    # Нет ключа response
    if RESPONSE not in response:
        # Ошибка нужен обязательный ключ
        raise MandatoryKeyError(RESPONSE)
    # если все хорошо, то
    # получаем код ответа
    code = response[RESPONSE]
    # длина кода не 3 символа
    if len(str(code)) != 3:
        # Ошибка неверная длина кода ошибки
        raise ResponseCodeLenError(code)
    # неправильные коды символов
    if code not in RESPONSE_CODES:
        # ошибка неверный код ответа
        raise ResponseCodeError(code)
    # возвращаем ответ
    return response


if __name__ == '__main__':
    # Создаем сокет
    client = socket(AF_INET, SOCK_STREAM)
    # Пытаемся получить параметры скрипта
    # если ip-адрес указан в параметрах -p <addr>
    try:
        addr = sys.argv[1]
    # если ip-адрес не указан в параметрах
    except IndexError:
        addr = 'localhost'
    # если порт указан в параметрах
    try:
        port = int(sys.argv[2])
    # если порт не указан в параметрах
    except IndexError:
        port = 7777
    # если порт - не целое число
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)
    # Соединяемся с сервером
    client.connect((addr, port))
    # Сформируем сообщение серверу
    presence = create_presence()
    # Отправим сообщение
    send_message(client, presence)
    # Получим ответ
    response = get_message(client)
    # Разоберем ответ
    response = translate_message(response)
    print(response)
