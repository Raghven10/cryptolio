from django import forms
from django.forms import ModelForm

from apps.home.models import Asset  


class OrderForm(ModelForm):     
    class Meta:
        model = Asset
        fields = '__all__'