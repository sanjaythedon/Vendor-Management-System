from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from vendors.models import Vendor
from vendors.serializers import VendorSerializer


@api_view(['GET', 'POST', 'DELETE'])
def vendors(request):
    try:
        if request.method == 'POST':
            create_vendor = Vendor.objects.create(**request.data)
            return Response({
                "message": "Vendor Created"
            })
        elif request.method == 'GET':
            vendor = Vendor.objects.all()
            serialized = VendorSerializer(vendor, many=True)
            return Response(serialized.data)

    except Exception as err:
        print(err)