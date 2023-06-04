from django import forms

from model_forms.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "age"]
