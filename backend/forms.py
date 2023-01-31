from django import forms
from .models import *

class formordersupdate(forms.ModelForm):
    class Meta:
        model = transaksitopup
        fields = ['statustransaksiid', 'invoice']
        labels = {
            'statustransaksiid': 'Status',
            'invoice': 'Invoice',
        }
        widgets = {
            'statustransaksiid': forms.HiddenInput(attrs={'value': '2','class': 'form-control'}),
            'invoice': forms.HiddenInput(attrs={'class': 'form-control'}),
        }