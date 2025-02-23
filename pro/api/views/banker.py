from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView, status
from rest_framework.response import Response

from ..permissions import BankGroupPermission
from ..serializers.fund import FundSerializer, AccountSerializer
from ..serializers.loan import LoanSerializer, LoanStatusSerializer
from ..serializers.bank import LoanDetailsSerializer

from ..models.provider import Fund
from ..models.banker import Total_money, LoanDetails
from ..models.customer import Loan






"""
API View to manage loan details such as minimum and maximum loan amounts.
Only accessible by users with BankGroupPermission.
"""
class ChangeLoanDetails(APIView):


    permission_classes = [BankGroupPermission]

    
    """
    Retrieve the current minimum and maximum loan limits.
    """
    def get(self, request):
        loan_details = get_object_or_404(LoanDetails, id=1)
        return Response({"min": loan_details.min_loan, "max": loan_details.max_loan}, status=status.HTTP_200_OK)
    
    """
    Update the minimum and maximum loan limits.
    Redirects to 'change-min-max' after a successful update.
    """
    def put(self, request):

        loan_details = get_object_or_404(LoanDetails, id=1)
        serializer = LoanDetailsSerializer(loan_details, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()

        return redirect('change-min-max')

"""
API View to manage fund requests from providers.
"""
class FundRequests(APIView):


    permission_classes = [BankGroupPermission]

    """
    Retrieve all fund requests.
    """
    def get(self, request, fund_id=None):

        fund_requests = Fund.objects.all()
        serializer = FundSerializer(fund_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Update the status of a fund request.
    If a request is approved, an account is created for the provider, and bank funds are updated.
    """
    def put(self, request, fund_id):
    
        fund = get_object_or_404(Fund, id=fund_id)
        prev_status = fund.status if fund else None
        serializer = FundSerializer(fund, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            # If the fund request is approved, create an account for the provider
            if prev_status == 'PENDING' and serializer.data['status'] == 'APPROVED':
                acc_data = {'account_user': fund.provider.id, 'account_profit': 0.0}
                acc_ser = AccountSerializer(data=acc_data)

                # Increase the bank's total money
                bank_money = get_object_or_404(Total_money, id=1)
                bank_money.total_money += fund.total_budget
                bank_money.save()

                if acc_ser.is_valid():
                    acc_ser.save()
                    print('Account Created')

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




"""
API View to manage loan requests from customers.
"""
class LoanRequests(APIView):

    permission_classes = [BankGroupPermission]


    """
        Retrieve all loan requests.
    """
    def get(self, request):
        
        loan_requests = Loan.objects.all()
        serializer = LoanSerializer(loan_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
        Update the status of a loan request.
        If approved, a LoanStatus entry is created, and the bank's funds are adjusted.
    """
    def put(self, request, loan_id):

        loan = get_object_or_404(Loan, id=loan_id)
        prev_status = loan.status if loan else None
        serializer = LoanSerializer(loan, data=request.data, partial=True)

        total_money = get_object_or_404(Total_money, id=1)

        if serializer.is_valid() and float(loan.loan_amount) < float(total_money.total_money):
            serializer.save()

            # If the loan is approved, create an account for the customer
            if prev_status == 'PENDING' and serializer.data['status'] == 'APPROVED':
                acc_data = {'customer': loan.customer.id, 'Installments_paid': 0, 'duration_left': loan.Installments}
                acc_ser = LoanStatusSerializer(data=acc_data)

                # Deduct loan amount from the bank's total money
                total_money.total_money -= loan.loan_amount
                total_money.save()

                if acc_ser.is_valid():
                    acc_ser.save()
                    print('Account Created')

        else:
            return HttpResponse("Total Money Less Than Loan Amount", status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)
