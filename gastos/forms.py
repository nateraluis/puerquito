from django.forms import ModelForm
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class CreateExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ["date", "amount", "currency", "category", "description", "household"]
        widgets = {
            "date": forms.DateInput(
                format=("%d/%m/%Y"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Selecciona una fecha",
                    "type": "date",
                },
            ),
        }
