from rest_framework import serializers
from ..models.banker import *



class LoanDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanDetails
        fields =['min_loan', 'max_loan',]
