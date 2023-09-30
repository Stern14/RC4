from django.http import HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Robot
from .services import create_new_robot, create_summary_robots


@csrf_exempt
def api_robots(request):
    '''
    API-endpoint для создания в БД записи о новом роботе
    '''

    if request.method == "POST":
        result = create_new_robot(request)
        return HttpResponse(result)
    
    if request.method == 'GET':
        return HttpResponse('Чтобы сохранить в БД новую запись о роботе, отправьте POST-запрос с данными в формате JSON')


def total_week(request):
    '''
    Создает и отправлят Excel-файл со сводкой по суммарным показателям производства роботов за последнюю неделю.
    '''

    if request.method == 'GET':
        create_summary_robots(Robot.objects.all())

        try:
            return FileResponse(open('total_week.xlsx', 'rb'))
        except:
            return HttpResponse('<h1>За последнюю неделю роботов не было произведено</h1>')
