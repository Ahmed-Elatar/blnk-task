from django.shortcuts import render,redirect,get_object_or_404


from django.http import HttpResponse 
from rest_framework.views import APIView ,status
from rest_framework.response import Response

from ..permissions import BankGroupPermission

from ..serializers.fund import FundSerializer ,AccountSerializer
from ..serializers.loan import LoanSerializer ,LoanStatusSerializer
from ..serializers.bank import LoanDetailsSerializer

from ..models.provider import Fund,Account
from ..models.banker import Total_money , LoanDetails
from ..models.customer import Loan





class ChangeLoanDetails(APIView):
    permission_classes = [BankGroupPermission]

    def get(self,request):
        loan_details = LoanDetails.objects.filter(id=1).first()
        return Response({"min":loan_details.min_loan,"max":loan_details.max_loan}, status=status.HTTP_200_OK)

    def put(self,request):
        loan_details = get_object_or_404(LoanDetails,id=1)
        serializer = LoanDetailsSerializer(loan_details, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid() :
            print(123)

            serializer.save()
            

        return redirect('change-min-max')



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
        if serializer.is_valid() :
            
            serializer.save()
            
            # check if request approved ==>>> then create account for the provider
            if prev_status == 'PENDING' and serializer.data['status'] == 'APPROVED':

                acc_data    = {'account_user':fund.provider.id,'account_profit': 0.0}
                acc_ser = AccountSerializer(data=acc_data)
                
                bank_money = Total_money.objects.filter(id=1).first()
                bank_money.total_money += fund.total_budget
                bank_money.save()
                ## Save the Ticker instance after the Validation
                if acc_ser.is_valid():
                    acc_ser.save()
                    
                    print('Account Created')


            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class LoanRequests(APIView):
    permission_classes = [BankGroupPermission]
    
    

    
    def get(self,request):

        loan_requests = Loan.objects.all()
        serializer = LoanSerializer(loan_requests, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request, loan_id):
        loan = get_object_or_404(Loan, id=loan_id)
        prev_status =None
        if loan :
            prev_status  = loan.status
        serializer = LoanSerializer(loan, data=request.data, partial=True)
        total_money=Total_money.objects.filter(id=1).first()
        if serializer.is_valid() and float(loan.loan_amount) < float(total_money.total_money):
            serializer.save()
            # check if request approved ==>>> then create status for the customer
            if prev_status == 'PENDING' and serializer.data['status'] == 'APPROVED':

                acc_data    = {'customer':loan.customer.id,'Installments_paid': 0,'duration_left': loan.Installments}
                acc_ser = LoanStatusSerializer(data=acc_data)
                
                bank_money = Total_money.objects.filter(id=1).first()
                bank_money.total_money -= loan.loan_amount
                bank_money.save()
                ## Save the Ticker instance after the Validation
                if acc_ser.is_valid():
                    acc_ser.save()
                    
                    print('Account Created')
        else:
            return HttpResponse("Total Money Less Than Loan Amount", status=status.HTTP_400_BAD_REQUEST)
        

        return Response(serializer.data, status=status.HTTP_200_OK)
        