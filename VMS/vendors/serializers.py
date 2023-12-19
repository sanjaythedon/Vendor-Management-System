from rest_framework import serializers
from vendors import models


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = "__all__"


class VendorPerformanceMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        exclude = ['id', 'name', 'contact_details', 'address']


class PerformanceMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PerformanceHistory
        fields = '__all__'
