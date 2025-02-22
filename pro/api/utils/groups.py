from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

Loan_Provider = Group.objects.get_or_create(name='Loan_Provider')

# permission = Permission.objects.create(codename='can_add_project',
#                                    name='Can add project',
#                                    content_type=ct)
# Loan_Provider.permissions.add(permission)


Loan_Customer = Group.objects.get_or_create(name='Loan_Customer')

# permission = Permission.objects.create(codename='can_add_project',
#                                    name='Can add project',
#                                    content_type=ct)
# Loan_Customer.permissions.add(permission)


Bank_personal = Group.objects.get_or_create(name='Bank_personal')

# permission = Permission.objects.create(codename='can_add_project',
#                                    name='Can add project',
#                                    content_type=ct)
# Bank_personal.permissions.add(permission)
