from django import forms
from django.forms import ModelForm
from Client.models import *
from SecretUrl.models import *
from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField

class ClientForm(forms.ModelForm):
    
    class Meta:
        model= Client
        fields='__all__'
        
class SecretUrlForm(forms.ModelForm):
    
    class Meta:
        model= SecretUrl
        fields='__all__'
        


