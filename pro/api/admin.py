from django.contrib import admin
from .models.provider import *
from .models.customer import *
from .models.banker import *

# Register your models here.



admin.site.register(Fund)
admin.site.register(Account)
admin.site.register(LoanDetails)    
admin.site.register(Loan)
admin.site.register(LoanStatus)
admin.site.register(Total_money)



