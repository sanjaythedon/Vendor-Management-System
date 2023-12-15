from rest_framework import serializers
from orders import models
import uuid
import json
from datetime import datetime


class OrderSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(required=False)

    class Meta:
        model = models.PurchaseOrders
        fields = '__all__'


class DeliveryDateSetSerializer(OrderSerializer):
    vendor = serializers.CharField(required=False)
    items = serializers.JSONField(required=False)
    delivery_date = serializers.DateTimeField(required=True)


class DeliveredSerializer(OrderSerializer):
    vendor = serializers.CharField(required=False)
    items = serializers.JSONField(required=False)
    quality = serializers.FloatField(required=True)



