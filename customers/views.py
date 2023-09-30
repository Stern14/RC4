from django.shortcuts import render, redirect
from .forms import CustomerForm
from .services import customer_login


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {"form": CustomerForm()})

    if request.method == 'POST':
        customer_login(request)

        return redirect(f'/orders/create')
