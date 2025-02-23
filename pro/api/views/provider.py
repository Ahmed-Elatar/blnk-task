from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView, status
from rest_framework.response import Response

from ..permissions import ProviderGroupPermission
from ..serializers.fund import FundSerializer, AccountSerializer
from ..models.provider import Fund, Account
from ..forms.provider import FundForm
from django.http import HttpResponse, JsonResponse


# ===================================================================================
#                                  Helper Views
# ===================================================================================

def pending(request):
    """
    Renders the 'pending.html' template for providers awaiting approval.
    """
    return render(request, "pending.html", status=status.HTTP_200_OK)


# ===================================================================================
#                         Provider Account & Fund Request Views
# ===================================================================================

class ProviderAccountDetails(APIView):
    """
    Handles the retrieval of provider account details.
    
    - If the fund request is still pending, redirects to the pending page.
    - If the fund request is rejected, renders the rejected page.
    - If an account exists, returns the account details.
    """
    permission_classes = [ProviderGroupPermission]

    def get(self, request):
        fund_details = Fund.objects.filter(provider=request.user).first()
        
        if fund_details and fund_details.status == 'PENDING':
            return redirect('pending')
        elif fund_details and fund_details.status == 'REJECTED':
            return render(request, "rejected.html", status=status.HTTP_200_OK)

        acc_details = Account.objects.filter(account_user=request.user).first()
        if acc_details is None:
            return Response({"message": "Account not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AccountSerializer(acc_details)
        print(serializer.data)  # Debugging output
        return render(request, "account_details.html", {"account": serializer.data, "name": request.user.username})


class ProviderFundRequest(APIView):
    """
    Handles the provider's fund request process.
    
    - GET: Displays the fund request form if no account exists.
    - POST: Submits the fund request, associates it with the user, and sets it to 'PENDING'.
    """
    permission_classes = [ProviderGroupPermission]

    def get(self, request):
        ifexists = Account.objects.filter(account_user=request.user).first()

        if ifexists is not None:
            return redirect('account-details')  # Redirect if account already exists
        else:
            form = FundForm()
            return render(request, "request_fund.html", {"form": form}, status=status.HTTP_200_OK)

    def post(self, request):
        form = FundForm(request.POST)
        if form.is_valid():
            fund = form.save(commit=False)
            fund.provider = request.user  # Assign the logged-in user as the provider
            fund.status = 'PENDING'  # Set request status as pending
            fund.save()

        return redirect('account-details')  # Redirect to account details page


# ===================================================================================
#                                Test / Index View
# ===================================================================================

def index(request):
    """
    Returns a simple 'Hello World' response for testing purposes.
    """
    return HttpResponse('Hello World.././/.')
