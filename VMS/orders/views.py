from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response

from orders.signals import UpdateSignalSender
from orders.models import PurchaseOrders
from orders.serializers import (OrderSerializer,
                                DeliveryDateSetSerializer,
                                DeliveredSerializer)

from datetime import datetime


class Orders(generics.ListCreateAPIView):
    queryset = PurchaseOrders.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Order(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrders.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class AcknowledgeOrder(generics.UpdateAPIView):
#     queryset = PurchaseOrders.objects.all()
#     serializer_class = DeliveryDateSetSerializer
#     lookup_field = 'id'
#
#     def put(self, request, *args, **kwargs):
        # try:
        # print(request.data)
        # print(id)
        # queryset = PurchaseOrders.objects.filter(id=id)
        # delivery_date = request.data['delivery_date']
        # status = 'pending'
        # acknowledgment_date = datetime.now()
        # queryset.update(delivery_date=delivery_date,
        #                 status=status,
        #                 acknowledgment_date=acknowledgment_date)
        # print('Update is done')
        # print(request.data)
        # print(args)
        # print(kwargs)
        # kwargs['update_fields'] = 'acknowledgement_date'
        # UpdateSignalSender.send_signal()
        # request.data['status'] = 'pending'
        # request.data['acknowledgment_date'] = datetime.now()
        # return self.update(request, update_fields='acknowledgement_date', *args, **kwargs)

    # except Exception as err:
    #     print(err)

class AcknowledgeOrder(generics.GenericAPIView):
    queryset = PurchaseOrders.objects.all()
    serializer_class = DeliveryDateSetSerializer
    lookup_field = 'id'

    def put(self, request, id, *args, **kwargs):
        try:
            po = PurchaseOrders.objects.get(id=id)
            po.acknowledgment_date = datetime.now()
            po.delivery_date = request.data['delivery_date']
            a = po.save(update_fields=['acknowledgment_date', 'delivery_date'])
            print(a)
            # order = self.queryset.filter(id=id)
            # serializer = self.serializer_class(instance=order, data=request.data)
            # if serializer.is_valid():
            #     a = serializer.save()
            #     print(a)
            #     return Response({
            #         "message": "DOne"
            #     }, status=200)
            # else:
            #     return Response({
            #         "message": " Not DOne"
            #     }, status=200)
            return Response({
                    "message": "DOne"
                }, status=200)

        except Exception as err:
            print(err)

        # print(request.data)
        # print(kwargs)
        # return Response({
        #     "message": "DOne"
        # }, status=200)


# class DeliveredOrder(generics.UpdateAPIView):
#     queryset = PurchaseOrders.objects.all()
#     serializer_class = DeliveredSerializer
#     lookup_field = 'id'
#
#     def put(self, request, *args, **kwargs):
#         # try:
#         request.data['status'] = "completed"
#         return self.update(request, *args, **kwargs)
    # except Exception as err:
    #     print(err)

class DeliveredOrder(generics.GenericAPIView):
    queryset = PurchaseOrders.objects.all()
    serializer_class = DeliveryDateSetSerializer
    lookup_field = 'id'

    def put(self, request, id, *args, **kwargs):
        po = PurchaseOrders.objects.get(id=id)
        po.status = 'completed'
        po.quality = request.data['quality']
        po.save()
        return Response({
            "message": "Delivered"
        }, status=200)

