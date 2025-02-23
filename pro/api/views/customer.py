from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.models import User, Group
from ..forms.customer import *

from django.http import HttpResponse ,JsonResponse

from rest_framework.views import APIView ,status
from rest_framework.response import Response

from ..permissions import CustomerGroupPermission

from ..serializers.loan import LoanSerializer ,LoanStatusSerializer

from ..models.customer import Loan,LoanStatus
from ..models.banker import Total_money










class CustomerLoanRequests(APIView):
    # permission_classes = [CustomerGroupPermission]
    
    

    
    def get(self,request):

        form = LoanForm()
        return render(request,"request_loan.html" ,{"form":form},status=status.HTTP_200_OK)
    
    def post(self,request):
    
        form = LoanForm(request.POST)
        if form.is_valid():
            
            loan = form.save(commit=False)
            loan.customer = request.user  
            loan.status = 'PENDING'  
            loan.save()  
        
        
        return redirect('loan-status')
    




class CustomerLoanDetails(APIView):
    permission_classes = [CustomerGroupPermission]
    
    

    
    def get(self, request):
        loan_details=Loan.objects.filter(customer=request.user).first()
        if loan_details.status == 'PENDING':
            return redirect('pending')
        elif loan_details.status == 'REJECTED':
            return render(request, "rejected.html", status=status.HTTP_200_OK)
            



        loan_details = LoanStatus.objects.filter(customer=request.user).first()
        if loan_details is None:
            return Response({"message": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LoanStatusSerializer(loan_details)
        print(serializer.data)
        return render(request, "loan_status.html", {"loan_status": serializer.data,"name":request.user.username})
    
    def post(self, request):
        
        loan_details = LoanStatus.objects.filter(customer=request.user).first()
        
        bank_money = Total_money.objects.filter(id=1).first()
        bank_money.total_money += loan_details.single_Installments
        bank_money.save()

        loan_details.Installments_paid += 1
        loan_details.duration_left -= 1
        loan_details.save()
        
        
        
        return redirect('loan-status')
    