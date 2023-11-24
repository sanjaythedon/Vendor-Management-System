from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response

from orders.models import PurchaseOrders
from orders.serializers import (OrderSerializer,
                                DeliveryDateChangeSerializer,
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


class AcknowledgeOrder(generics.UpdateAPIView):
    queryset = PurchaseOrders.objects.all()
    serializer_class = DeliveryDateChangeSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
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
            print(request.data)
            print(args)
            print(kwargs)
            request.data['status'] = 'pending'
            request.data['acknowledgment_date'] = datetime.now()
            return self.update(request, *args, **kwargs)

        # except Exception as err:
        #     print(err)


class DeliveredOrder(generics.UpdateAPIView):
    queryset = PurchaseOrders.objects.all()
    serializer_class = DeliveredSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        # try:
            request.data['status'] = "completed"
            return self.update(request, *args, **kwargs)
        # except Exception as err:
        #     print(err)







