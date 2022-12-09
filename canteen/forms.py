from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateStaffForm(UserCreationForm):
    phone = forms.CharField(max_length=10)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    pincode = forms.CharField(max_length=6)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "phone",
            "city",
            "state",
            "pincode",
        ]


class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        enctype = "multipart/form-data"
