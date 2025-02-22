from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models import Q

















# class Fund(models.Model):
#     provider = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='Fund',
#         limit_choices_to={
#             'groups__name': 'Loan_Provider'  # Filter users in the 'Loan Provider' group
#         }
#     )
    
#     total_budget = models.FloatField()

#     status = models.CharField(
#         max_length=20,
#         choices=[
#             ('PENDING', 'Pending'),
#             ('APPROVED', 'Approved'),
#             ('REJECTED', 'Rejected'),
#         ],
#         default='PENDING'
#     ) 

#     def __str__(self):
#         return self.provider.username




