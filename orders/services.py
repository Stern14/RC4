from customers.models import Customer
from .forms import OrderForm
from .models import Order


def create_order(request):
    order = OrderForm(request.POST)
    if order.is_valid():
        customer_id = request.session.get('customer_id')
        serial = order.cleaned_data['serial']
        Order(customer=Customer(id=customer_id), robot_serial=serial).save()
        state = f'Order robot {serial} for user: {customer_id} create'

    else:
        state = f'Serial is not correct! Repet please!'

    return state
