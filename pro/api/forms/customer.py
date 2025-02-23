from django import forms 

from ..models.customer import *
from ..models.banker import LoanDetails

min_loan = LoanDetails.objects.filter(id=1).first().min_loan
max_loan = LoanDetails.objects.filter(id=1).first().max_loan


class LoanForm(forms.ModelForm):
    
    loan_amount = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': min_loan, 'max': max_loan})
    )
    
    class Meta:
        model = Loan
        fields = ['loan_amount', 'Installments', ]  
    