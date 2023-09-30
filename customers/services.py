from .models import Customer
from .forms import CustomerForm


def customer_login(request):
    customer = CustomerForm(request.POST)
    if customer.is_valid():
        email = customer.cleaned_data['email']
        customers = Customer.objects.filter(email = email)
        if customers.count() == 0:
            Customer(email = email).save()
        request.session['customer_id'] = Customer.objects.filter(email=email)[0].id