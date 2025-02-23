from rest_framework import serializers
from ..models.provider import *



class FundSerializer(serializers.ModelSerializer):
    provider_username = serializers.CharField(source="provider.username", read_only=True)

    class Meta:
        model = Fund
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


