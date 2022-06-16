from rest_framework import serializers

from .models import Test

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'order_id', 'cost_usd', 'date', 'cost_rub']