from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models import Q

















class LoanDetails(models.Model):
    min_loan = models.FloatField()
    max_loan = models.FloatField()
    


class Total_money(models.Model):
    total_money = models.FloatField(default=0)

    def __str__(self):
        return str(self.total_money)
