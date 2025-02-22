
from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.models import User, Group
from ..forms.auth import *

from django.http import HttpResponse ,JsonResponse

from rest_framework.views import APIView ,status
from rest_framework.generics import ListAPIView , RetrieveDestroyAPIView
from rest_framework.response import Response
from django.http import HttpResponseForbidden

from ..permissions import ProviderGroupPermission


# Create your views here.


def index(request):
    return HttpResponse('Hello World.././/.')




def provide_loan(request):
    if not request.user.groups.filter(name='Loan_Provider').exists():
        return HttpResponseForbidden("Access Denied: You are not in the Loan_Provider group.")
    return HttpResponse("You are in the Loan_Provider group!")



def fund_status(request):
    if not request.user.groups.filter(name='Loan_Provider').exists():
        return HttpResponseForbidden("Access Denied: You are not in the Loan_Provider group.")
    return HttpResponse("You are in the Loan_Provider group!")




class TakeSymbol(APIView):
    permission_classes = [ProviderGroupPermission]
    
    
    def post(self,request):
        
        # result =send_data_to_fastapi({"sender":str(request.user) ,"symbol": symbol.upper() })
        # print(123)
        return HttpResponse("ASd")
        return JsonResponse({'Data-Status': 'Recived'}, status=status.HTTP_200_OK)
    
    def get(self,request):
        return HttpResponse(123)

