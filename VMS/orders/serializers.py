from rest_framework import serializers
from orders import models
import uuid
import json
from datetime import datetime


class OrderSerializer(serializers.ModelSerializer):
    po_number = serializers.CharField(required=False)
    quantity = serializers.IntegerField(required=False)
    delivery_date = serializers.DateTimeField(required=False)
    status = serializers.CharField(required=False)
    quality = serializers.FloatField(required=False)
    acknowledgment_date = serializers.DateTimeField(required=False)

    class Meta:
        model = models.PurchaseOrders
        fields = '__all__'


