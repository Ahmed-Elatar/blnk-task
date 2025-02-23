from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from ..forms.customer import *

from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView, status
from rest_framework.response import Response

from ..permissions import CustomerGroupPermission
from ..serializers.loan import LoanSerializer, LoanStatusSerializer
from ..models.customer import Loan, LoanStatus
from ..models.banker import Total_money


class CustomerLoanRequests(APIView):
    """
    API View for handling customer loan requests.
    Customers can request a loan by filling out a form.
    """

    permission_classes = [CustomerGroupPermission]

    def get(self, request):
        """
        Display the loan request form.
        """
        form = LoanForm()
        return render(request, "request_loan.html", {"form": form}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle loan request submissions.
        
        - Saves the loan with 'PENDING' status.
        - Assigns the requesting user as the customer.
        - Redirects to the loan status page after submission.
        """
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)  # Create Loan object without saving to the database yet
            loan.customer = request.user  # Assign the logged-in user as the customer
            loan.status = 'PENDING'  # Set the initial loan status to 'PENDING'
            loan.save()  # Save the loan request to the database
        
        return redirect('loan-status')  # Redirect to loan status page


class CustomerLoanDetails(APIView):
    """
    API View for retrieving loan details and making installment payments.
    """

    permission_classes = [CustomerGroupPermission]

    def get(self, request):
        """
        Retrieve the details of the customer's loan.

        - Redirects to 'pending' page if the loan status is PENDING.
        - Renders 'rejected' page if the loan status is REJECTED.
        - Fetches approved loan details and displays them.
        """
        loan_details = Loan.objects.filter(customer=request.user).first()

        # Redirect based on loan status
        if loan_details.status == 'PENDING':
            return redirect('pending')
        elif loan_details.status == 'REJECTED':
            return render(request, "rejected.html", status=status.HTTP_200_OK)

        # Fetch approved loan details
        loan_status = LoanStatus.objects.filter(customer=request.user).first()
        if loan_status is None:
            return Response({"message": "Account not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LoanStatusSerializer(loan_status)
        print(serializer.data)  # Debugging log for serialized data

        return render(request, "loan_status.html", {"loan_status": serializer.data, "name": request.user.username})

    def post(self, request):
        """
        Process an installment payment for the customer's loan.

        - Deducts the installment amount from the bank's total money.
        - Updates the customer's installment payments and remaining duration.
        - Redirects to the loan status page after payment.
        """
        loan_details = LoanStatus.objects.filter(customer=request.user).first()
        
        if not loan_details:
            return Response({"message": "Loan not found"}, status=status.HTTP_404_NOT_FOUND)

        bank_money = Total_money.objects.filter(id=1).first()
        
        # Increase the bank's total money by the installment amount
        bank_money.total_money += loan_details.single_Installments
        bank_money.save()

        # Update the customer's loan payment details
        loan_details.Installments_paid += 1
        loan_details.duration_left -= 1
        loan_details.save()
        
        return redirect('loan-status')  # Redirect to the loan status page after payment
