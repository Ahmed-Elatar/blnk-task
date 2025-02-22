from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models import Q

















class Fund(models.Model):
    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Fund',
        limit_choices_to={
            'groups__name': 'Loan_Provider'  # Filter users in the 'Loan Provider' group
        }
    )
    
    total_budget = models.FloatField()

    status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending'),
            ('APPROVED', 'Approved'),
            ('REJECTED', 'Rejected'),
        ],
        default='PENDING'
    ) 

    def __str__(self):
        return self.provider.username





class Account(models.Model):
    account_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Account',

        limit_choices_to=Q(groups__name='Loan_Provider') | Q(groups__name='Loan_Customer')
    )
    
    total_budget = models.FloatField(default=0.0)

    account_profit = models.FloatField()


    def save(self, *args, **kwargs):
        """ Sync total_budget with Fund when Account is saved """
        fund = Fund.objects.filter(provider=self.account_user).first()
        
        if fund:
            self.total_budget = fund.total_budget  # Sync Fund to Account
        
        super().save(*args, **kwargs) 
     

    def __str__(self):
        return self.account_user.username




