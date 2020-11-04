from django import forms
from .models import Thread


class CreateThreadForm(forms.ModelForm):
  class Meta:
    model = Thread
    fields = 
