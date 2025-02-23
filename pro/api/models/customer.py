from django.contrib.auth.models import User
from django.db import models

















class Loan(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Loan',
        limit_choices_to={
            'groups__name': 'Loan_Customer'  # Filter users in the 'Loan Customer' group
        }
    )
    
    loan_amount = models.FloatField()
    Installments = models.IntegerField(default=1)
    
    status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending'),
            ('APPROVED', 'Approved'),
            ('REJECTED', 'Rejected'),
            ('FINISHED', 'Finished'),
        ],
        default='PENDING'
    )

    interst_rate = models.FloatField(default=0.1) 

    def __str__(self):
        return self.customer.username





class LoanStatus(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='LoanStatus',
        limit_choices_to={
            'groups__name': 'Loan_Customer'  # Filter users in the 'Loan Customer' group
        }
    )
    
    single_Installments = models.FloatField(default=1)
    Installments_paid = models.IntegerField(default=0)

    
    duration_left = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        """ Sync total_budget with Fund when Account is saved """
        loan = Loan.objects.filter(customer=self.customer).first()
        
        if loan:
            self.single_Installments = loan.loan_amount / loan.Installments
            self.single_Installments += self.single_Installments * loan.interst_rate

        super().save(*args, **kwargs) 
     

    def __str__(self):
        return self.customer.username

