from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_slug
from time import strptime


def validate_even(data):
    model = data['model']
    version = data['version']
    date = data['created']

    if len(model) != 2:
        return f"Неккоректное наименование модели! Имя модели должно быть длиной в 2(два) символа"
    try:
        validate_slug(model)
    except ValidationError:
        return 'Неккоректное наименование модели! Имя модели состоит только из латинских букв, цифр, символов подчеркивания или дефисов'

    if len(version) != 2:
        return "Неккоректное наименование версии! Имя версии должно быть длиной в 2(два) символа"
    try:
        validate_slug(version)
    except ValidationError:
        return 'Неккоректное наименование модели! Имя модели состоит только из латинских букв, цифр, символов подчеркивания или дефисов'

    try:
        strptime(date, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return f'Не правильно введено время!\nПравильный формат времени: ГГ-ММ-ДД ЧЧ:ММ:СС\nПравильный пример: 2022-12-31 23:59:59\nИ что отправил ты: {date}'

    return True
