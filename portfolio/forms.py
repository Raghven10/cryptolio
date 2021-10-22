from django.forms import ModelForm

from .models import Asset, User


class AddNewAsset(ModelForm):
   class Meta:
    model = Asset
    fields = '__all__'

class AddNewUser(ModelForm):
   class Meta:
    model = User
    fields = '__all__'
