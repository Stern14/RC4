import openpyxl

from django.dispatch import receiver
from django.db.models.signals import post_save

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Robot


def send_message(email, instance):
    data = {
        'model': instance.model,
        'version': instance.version,
    }

    html_body = render_to_string('email_message.html', data)

    msg = EmailMultiAlternatives(subject='Интересуемый робот в наличии', to = [email])
    msg.attach_alternative(html_body, 'text/html')
    msg.send()

@receiver(post_save, sender=Robot)
def check_waiting_list(instance, **kwargs):
    serial = instance.serial

    try:
        wb = openpyxl.load_workbook('waiting_list.xlsx')
        sheet = wb.active

        row = 1
        while True:
            if sheet['A1'].value == None:
                print('Лист ожидания пуст')
                break

            if row > sheet.max_row:
                break

            if sheet[f'A{row}'].value == serial:
                email_customer = sheet[f'B{row}'].value
                send_message(email_customer, instance)
                sheet.delete_rows(row)

            else:
                row += 1

            wb.save('waiting_list.xlsx')

    except:
        print('Лист ожидания пуст')
