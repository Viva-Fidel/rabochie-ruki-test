from rest_framework import serializers

from .models import Organization, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class GetBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["inn", "balance"]
