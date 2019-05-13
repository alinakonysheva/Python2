import json

# Кодировка
ENCODING = 'utf-8'


def dict_to_bytes(message_dict):
    # Проверям, что пришел словарь
    if isinstance(message_dict, dict):
        # Преобразуем словарь в json
        jmessage = json.dumps(message_dict)
        # Переводим json в байты
        bmessage = jmessage.encode(ENCODING)
        # Возвращаем байты
        return bmessage
    else:
        raise TypeError


def bytes_to_dict(message_bytes):

    # Если переданы байты
    if isinstance(message_bytes, bytes):
        # Декодируем
        jmessage = message_bytes.decode(ENCODING)
        # Из json делаем словарь
        message = json.loads(jmessage)
        # Если там был словарь
        if isinstance(message, dict):
            # Возвращаем сообщение
            return message
        else:
            # Нам прислали неверный тип
            raise TypeError
    else:
        # Передан неверный тип
        raise TypeError


def send_message(sock, message):
    # Словарь переводим в байты
    bprescence = dict_to_bytes(message)
    # Отправляем
    sock.send(bprescence)


def get_message(sock):
    # Получаем байты
    bresponse = sock.recv(1024)
    # переводим байты в словарь
    response = bytes_to_dict(bresponse)
    # возвращаем словарь
    return response
