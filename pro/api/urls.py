from django.urls import path 
from .views.authentication import *
from .views.provider import *
from .views.banker import *
from .views.customer import *


urlpatterns = [
    path('',index ,name='index') ,

    ####################################################
    #######    Authentication  #########################
    path('login/',user_login ,name='login') ,
    path('singup/',user_signup ,name='signup') ,
    path('logout/',user_logout ,name='logout') ,
    ####################################################

    ####################################################
    #######    Provider  #########################
    path('pending/',pending ,name='pending') ,
    
    path('provider-fund-request/',ProviderFundRequest.as_view() ,name='fund-request') ,
    path('provider-account-details/',ProviderAccountDetails.as_view() ,name='account-details') ,


    ####################################################
    #######    Banker  #########################
    path('bank-change-min-max/',ChangeLoanDetails.as_view() ,name='change-min-max') ,
    path('bank-fund-requests/',FundRequests.as_view() ,name='bank-fund-requests') ,
    path('bank-fund-request/<int:fund_id>/',FundRequests.as_view() ,name='bank-fund-request') ,
    path('bank-loan-request/<int:loan_id>/',LoanRequests.as_view() ,name='bank-loan-request') ,
    path('bank-loan-requests/',LoanRequests.as_view() ,name='bank-loan-requests') ,


    ####################################################
    #######    Cusomer  #########################
    path('customer-loan-request/',CustomerLoanRequests.as_view() ,name='loan-requests') ,
    path('customer-loan-status/',CustomerLoanDetails.as_view() ,name='loan-status') ,
    




]
