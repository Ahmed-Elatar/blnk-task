from celery import shared_task
import time
from .models.provider import Account

from .models.banker import Total_money


@shared_task
def try_to_sleep():
    
    time.sleep(1)
    print("Done sleeping")

profit_percent = 0.1

@shared_task
def add_profit_to_provider():
    accounts = Account.objects.all()
    for account in accounts:
        
        ####################### Deduct profit from bank ##############################################
        bank_money = Total_money.objects.filter(id=1).first()
        bank_money.total_money -= (account.total_budget + account.account_profit ) * profit_percent
        bank_money.save()

        ###################### Add profit for each account#############################################3
        account.account_profit += (account.total_budget + account.account_profit ) * profit_percent
        account.save()

        

        print(f"Profit added to {account.account_user.username}")
    print("Done adding profit to providers")
    