from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from vendors.models import Vendor
from vendors.serializers import VendorSerializer


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def vendors(request, pk=None):
    try:
        if request.method == 'POST':
            Vendor.objects.create(**request.data)
            return Response({
                "message": "Vendor Created"
            })
        elif request.method == 'GET':
            if pk:
                vendor = Vendor.objects.filter(id=pk)
            else:
                vendor = Vendor.objects.all()
            serialized = VendorSerializer(vendor, many=True)
            return Response(serialized.data)
        elif request.method == 'DELETE':
            vendor = Vendor.objects.get(id=pk)
            vendor.delete()
            return Response({
                "message": f"{vendor} is deleted."
            })
        elif request.method == 'PUT':
            Vendor.objects.filter(id=pk).update(**request.data)
            vendor = Vendor.objects.filter(id=pk)
            serialized = VendorSerializer(vendor, many=True)
            return Response(serialized.data)

    except Exception as err:
        print(err)