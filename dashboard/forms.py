from django import forms
from crispy_forms.helper import FormHelper

class CarControlForm(forms.Form):
    speed = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'slider1', 'class': 'slider1', 'type':'range', 'step': '1', 'min': '-100', 'max': '100'}), required=True)
    helper = FormHelper()

    