from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from vendors.models import (Vendor,
                            PerformanceHistory)
from vendors.serializers import (VendorSerializer,
                                 PerformanceMetricsSerializer,
                                 VendorPerformanceMetricsSerializer)


# @api_view(['GET', 'POST', 'DELETE', 'PUT'])
# def vendors(request, pk=None):
#     try:
#         if request.method == 'POST':
#             Vendor.objects.create(**request.data)
#             return Response({
#                 "message": "Vendor Created"
#             })
#         elif request.method == 'GET':
#             if pk:
#                 vendor = Vendor.objects.filter(id=pk)
#             else:
#                 vendor = Vendor.objects.all()
#             serialized = VendorSerializer(vendor, many=True)
#             return Response(serialized.data)
#         elif request.method == 'DELETE':
#             vendor = Vendor.objects.get(id=pk)
#             vendor.delete()
#             return Response({
#                 "message": f"{vendor} is deleted."
#             })
#         elif request.method == 'PUT':
#             Vendor.objects.filter(id=pk).update(**request.data)
#             vendor = Vendor.objects.filter(id=pk)
#             serialized = VendorSerializer(vendor, many=True)
#             return Response(serialized.data)
#
#     except Exception as err:
#         print(err)

# class Vendors(APIView):
#
#     def get(self, request, pk=None):
#         if pk:
#             vendor = Vendor.objects.filter(id=pk)
#         else:
#             vendor = Vendor.objects.all()
#         serialized = VendorSerializer(vendor, many=True)
#         return Response(serialized.data)
#
#     def post(self, request):
#         Vendor.objects.create(**request.data)
#         return Response({
#             "message": "Vendor Created"
#         })
#
#     def put(self, request, pk):
#         Vendor.objects.filter(id=pk).update(**request.data)
#         vendor = Vendor.objects.filter(id=pk)
#         serialized = VendorSerializer(vendor, many=True)
#         return Response(serialized.data)
#
#     def delete(self, request, pk):
#         vendor = Vendor.objects.get(id=pk).delete()
#         return Response({
#             "message": f"{vendor} is deleted."
#         })


class VendorsList(generics.ListCreateAPIView):

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VendorsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PerformanceMetrics(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceMetricsSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PerformanceMetricsHistory(generics.ListAPIView):
    queryset = PerformanceHistory.objects.all()
    serializer_class = PerformanceMetricsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# class Summa(generics.GenericAPIView):
#     def get(self, *args, **kwargs):
#         return Response({
#             "msg": "Ommala mariyaathaiya vanthuru"
#         }, status=200)

# class GetAllVendors(APIView):
#     def get(self, *args, **kwargs):
#         vendor = Vendor.objects.all()
#         # print(list(vendor)[1].name)
#         ser = VendorSerializer(vendor, many=True)
#         # print(f"All vendors: {ser.data}")
#         return Response(ser.data)

# @api_view()
# def summa(request):
#     vendor = Vendor.objects.all()
#     print(vendor)
