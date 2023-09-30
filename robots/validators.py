from django.core.exceptions import ValidationError
from django.core.validators import validate_slug
from time import strptime


def len_and_slug(fields: dict):
    '''
    Валидация данных модели и версии робота. 
    Если данные валидны - возвращает True. Если нет - то причину ошибки.
    Аргумент fields - это словарь, который содержит данные о модели и версии робота 
    '''

    for key, value in fields.items():
        if len(value) != 2:
            return f"Неккоректное наименование {key}! Имя {key} должно быть длиной в 2(два) символа"

        try:
            validate_slug(value)
        except ValidationError:
            return f'Неккоректное наименование {key}! Имя {key} состоит только из латинских букв, цифр, символов подчеркивания или дефисов'

    return True


def validate_even(data: dict):
    '''
    Валидация входящих от пользователя данных о роботе.
    Если данные валидны - возвращает True. Если нет - то причину ошибки.
    Аргумент data - это словарь, который содержит входящие от пользователя данные о роботе
    '''

    model = data['model']
    version = data['version']
    date = data['created']
    fields = {'model': model, "version": version}
    valid = len_and_slug(fields)

    if valid == True:
        try:
            strptime(date, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return f'Не правильно введено время!\nПравильный формат времени: ГГ-ММ-ДД ЧЧ:ММ:СС\nПравильный пример: 2022-12-31 23:59:59\nИ что отправил ты: {date}'
        return True
    return valid