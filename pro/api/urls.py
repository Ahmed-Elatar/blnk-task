from django.urls import path 
from .views.authentication import *
from .views.provider import *
from .views.banker import *



urlpatterns = [
    path('',index ,name='index') ,

    ####################################################
    #######    Authentication  #########################
    path('login/',user_login ,name='login') ,
    path('singup/',user_signup ,name='signup') ,
    path('logout/',user_logout ,name='logout') ,
    ####################################################


    path('provider/',provide_loan ,name='provider') ,
    path('take/',TakeSymbol.as_view() ,name='fund') ,


    ####################################################
    #######    Banker  #########################
    path('fund-requests/',FundRequests.as_view() ,name='fund-requests') ,
    path('fund-requests/<int:fund_id>/',FundRequests.as_view() ,name='fund-request') ,



]
