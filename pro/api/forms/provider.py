from django import forms 

from ..models.provider import *


class FundForm(forms.ModelForm):
    class Meta:
        model = Fund
        fields = ['total_budget' ]
    