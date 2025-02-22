from django.contrib import admin
from .models.provider import *

# Register your models here.



admin.site.register(Fund)
admin.site.register(Account)

# @admin.register(LoanFund)
# class LoanFundAdmin(admin.ModelAdmin):

#     readonly_fields = ('available_funds',)  # Mark the field as read-only
#     list_display = ('provider', 'total_budget', 'available_funds')
    
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.groups.filter(name='Loan_Provider').exists():
#             # Show only loans for this provider
#             return qs.filter(provider=request.user)
#         return qs 


# @admin.register(Loan)
# class LoanAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'amount', 'term', 'status')

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.groups.filter(name='Loan_Provider').exists():
#             # Show only loans for this provider
#             return qs.filter( customer=request.user)
#         return qs
