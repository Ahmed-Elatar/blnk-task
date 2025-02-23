from django.shortcuts import render,redirect,get_object_or_404



from rest_framework.views import APIView ,status
from rest_framework.response import Response

from ..permissions import ProviderGroupPermission

from ..serializers.fund import FundSerializer ,AccountSerializer

from ..models.provider import Fund,Account

from ..forms.provider import FundForm




    
def pending(request):

    return render(request, "pending.html", status=status.HTTP_200_OK)










class ProviderAccountDetails(APIView):
    permission_classes = [ProviderGroupPermission]
    
    

    
    def get(self, request):
        fund_details=Fund.objects.filter(provider=request.user).first()
        if fund_details.status == 'PENDING':
            return redirect('pending')
        elif fund_details.status == 'REJECTED':
            return render(request, "rejected.html", status=status.HTTP_200_OK)
            


        acc_details = Account.objects.filter(account_user=request.user).first()
        if acc_details is None:
            return Response({"message": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AccountSerializer(acc_details)
        print(serializer.data)
        return render(request, "account_details.html", {"account": serializer.data,"name":request.user.username})
    
    
class ProviderFundRequest(APIView):
    permission_classes = [ProviderGroupPermission]
    
    

    
    def get(self, request):

        ifexists = Account.objects.filter(account_user=request.user).first()

        if ifexists is not None:
            return redirect('account-details')
        
        else:
            form = FundForm()
        
            return render(request, "request_fund.html",{"form":form} , status=status.HTTP_200_OK)
    
    
    def post(self, request):

        form = FundForm(request.POST)
        if form.is_valid():
            
            fund = form.save(commit=False)
            fund.provider = request.user  
            fund.status = 'PENDING'  
            fund.save()  
        
        
        return redirect('account-details')
    
    

# Create your views here.

from django.http import HttpResponse ,JsonResponse

def index(request):
    return HttpResponse('Hello World.././/.')




