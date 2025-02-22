from rest_framework import serializers
from ..models.provider import *



class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'



# class LoanFundSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LoanFund
#         fields = '__all__'
#         read_only_fields = ['available_funds']