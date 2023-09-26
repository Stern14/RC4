import json
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Robot
from .validators import validate_even


@csrf_exempt
def api_robots(request):

    if request.method == "POST":
        #Загружаем и проверяем на валидность входящие данные
        data: dict = json.loads(request.body.decode())
        validate = validate_even(data)

        #Если данные корректны - сохраняем их в БД
        if validate == True:
            robot: Robot = Robot(
                serial=f"{data['model']}-{data['version']}",
                model=data['model'],
                version=data['version'],
                created=data['created']
            )
            robot.save()
            
            return HttpResponse('Запись сохраненна')
        
        #Если нет - отправляем причину ошибки
        return HttpResponse(validate)
