
from ..models.banker import Total_money , LoanDetails



total_money, created = Total_money.objects.get_or_create(id=1, defaults={'total_money': 0.0})

loan_details, created = LoanDetails.objects.get_or_create(id=1, defaults={'min_loan': 1000.0 , 'max_loan': 1000000.0})