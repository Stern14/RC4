from django.shortcuts import render
from .services import create_order
from .forms import OrderForm

# Create your views here.


def create(request):
    if request.method == 'POST':
        state = create_order(request)
        return render(request, 'create_order.html', {"form": OrderForm(), "state": state})

    if request.method == 'GET':
        return render(request, 'create_order.html', {"form": OrderForm()})
