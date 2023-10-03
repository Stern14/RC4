import openpyxl

from customers.models import Customer
from robots.models import Robot

from .models import Order
from .forms import OrderForm


def robots_gt_orders(serial):

    count_orders = Order.objects.filter(robot_serial=serial).count()
    count_robots = Robot.objects.filter(serial=serial).count()

    if count_orders < count_robots:
        return True
    return False


def save_wait_list(request, serial):
    try:
        wb = openpyxl.load_workbook('waiting_list.xlsx')
    except:
        wb = openpyxl.Workbook()

    sheet = wb.active

    row = 1
    while True:
        if sheet[f'A{row}'].value == None:
            sheet[f'A{row}'].value = serial
            sheet[f'B{row}'].value = request.session.get('email')
            break
        row += 1
    wb.save('waiting_list.xlsx')
    wb.close()


def create_order(request):
    order = OrderForm(request.POST)
    if order.is_valid():
        serial = order.cleaned_data['serial']

        if robots_gt_orders(serial):
            customer_id = request.session.get('customer_id')
            Order(customer=Customer(id=customer_id),
                  robot_serial=serial).save()
            state = f'Заказ на робота серии {serial} для пользователя {customer_id} оформлен'

        else:
            save_wait_list(request, serial)
            state = 'Робота данной серии нет в наличии. Мы уведомим вас сразу, если в складе появиться экземпляр робота данной серии'
    else:
        state = 'Неверный формат запрашиваемой серии! Пример правильного формата: R2-D2'

    return state
