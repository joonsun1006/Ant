from rest_framework import serializers
from .models import DepositAndSavings


class DepositAndSavingsSerializer(serializers.ModelSerializer):
    class Meta():
        model = DepositAndSavings
        fields = '__all__'