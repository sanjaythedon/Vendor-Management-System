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


