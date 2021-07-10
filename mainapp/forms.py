from .models import AddItem
from django.forms import ModelForm, formset_factory
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class User_create_form(UserCreationForm):
    pass


class login_form(AuthenticationForm):
    pass


class Add_item_form(ModelForm):
    class Meta:
        model = AddItem
        fields = ['Title', 'password']


class Display_Item_Form(forms.Form):
    Title = forms.CharField(max_length=150, label="")
    password = forms.CharField(max_length=200, label="")


Display_formset = formset_factory(Display_Item_Form, extra=0)
