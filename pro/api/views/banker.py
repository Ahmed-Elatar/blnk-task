from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.models import User, Group
from ..forms.auth import *

from django.http import HttpResponse ,JsonResponse

from rest_framework.views import APIView ,status
from rest_framework.generics import ListAPIView , RetrieveDestroyAPIView
from rest_framework.response import Response
from django.http import HttpResponseForbidden

from ..permissions import BankGroupPermission

from ..serializers.fund import FundSerializer ,AccountSerializer












class FundRequests(APIView):
    permission_classes = [BankGroupPermission]
    
    

    
    def get(self,request,fund_id=None):

        fund_requests = Fund.objects.all()
        serializer = FundSerializer(fund_requests, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
    def put(self, request, fund_id):
        fund = get_object_or_404(Fund, id=fund_id)
        prev_status =None
        if fund :
            prev_status  = fund.status
        serializer = FundSerializer(fund, data=request.data, partial=True)
        if serializer.is_valid():
            
            serializer.save()
            
            # check if request approved ==>>> then create account for the provider
            if prev_status == 'PENDING' and serializer.data['status'] == 'APPROVED':

                acc_data    = {'account_user':fund.provider.id,'account_profit': 0.0}
                acc_ser = AccountSerializer(data=acc_data)
                
                ## Save the Ticker instance after the Validation
                if acc_ser.is_valid():
                    acc_ser.save()
                    print('Account Created')


            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        