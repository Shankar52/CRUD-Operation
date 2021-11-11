from django import forms
from crud.models import crudst
from django.core import validators

class stform(forms.ModelForm):
    class Meta:
        model=crudst
        fields="__all__"
