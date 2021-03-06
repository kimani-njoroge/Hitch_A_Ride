from django import forms
from .models import Driver, Car

class DriverProfileForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = ['user']


class CarProfileForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_brand','no_plate','no_seat']
