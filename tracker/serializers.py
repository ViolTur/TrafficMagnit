from rest_framework import serializers
from .models import Currency, RateHistory

class RateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RateHistory
        fields = ['id', 'rate', 'timestamp']


class CurrencySerializer(serializers.ModelSerializer):
    current_rate = serializers.SerializerMethodField()

    class Meta:
        model = Currency
        fields = ['id', 'code', 'name', 'iso_code', 'is_active', 'current_rate']

        extra_kwargs = {
            'code': {'required': True},
            'name': {'required': True},
            'iso_code': {'required': True},
        }

    def get_current_rate(self, obj):
        last_rate = obj.rates.order_by('-timestamp').first()
        return last_rate.rate if last_rate else None