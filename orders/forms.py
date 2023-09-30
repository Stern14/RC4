from django import forms
from django.core.validators import validate_slug


class OrderForm(forms.Form):
    serial = forms.CharField(max_length=5,min_length=5, validators=[validate_slug])