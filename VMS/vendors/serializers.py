from rest_framework import serializers


class VendorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    contact_details = serializers.CharField(max_length=999)
    address = serializers.CharField(max_length=999)
    vendor_code = serializers.CharField(max_length=20)