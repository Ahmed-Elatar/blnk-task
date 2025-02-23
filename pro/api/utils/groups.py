from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

Loan_Provider = Group.objects.get_or_create(name='Loan_Provider')



Loan_Customer = Group.objects.get_or_create(name='Loan_Customer')



Bank_personal = Group.objects.get_or_create(name='Bank_personal')

