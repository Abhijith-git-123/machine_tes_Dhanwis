from django import forms
from .models import register



class regForm(forms.ModelForm):
    class Meta:
        model = register
        fields = ['name','email','phone','password']
