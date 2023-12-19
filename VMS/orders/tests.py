from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from orders.models import PurchaseOrders
from vendors.models import Vendor

# Create your tests here.


class OrderTest(APITestCase):

    def setUp(self):
        self.vendor = Vendor.objects.create(name="Kohli",
                                            address="RCB",
                                            contact_details="18")
        self.po = PurchaseOrders.objects.create(vendor=self.vendor,
                                      items={
                                            "Apple": 100,
                                            "Orange": 200
                                        })

    def test_order_list(self):
        url = reverse('orders:orders')
        res = self.client.get(url)
        self.assertEquals(res.status_code, 200)

    def test_order_detail(self):
        url = reverse('orders:a_order', args=[1])
        res = self.client.get(url)
        self.assertEquals(res.status_code, 200)

    def test_order_by_vendor(self):
        url = reverse('orders:orders')
        res = self.client.get(url, {'vendor': self.vendor})
        # print(res.json())
        self.assertEquals(res.status_code, 200)

    def test_create_order(self):
        url = reverse('orders:orders')
        data = {
                "vendor": str(self.vendor),
                "items": {
                    "Apple": 100,
                    "Orange": 200
                }
            }
        res = self.client.post(url, data=data, format='json')
        self.assertEquals(res.status_code, 201)

    def test_delete_order(self):
        url = reverse('orders:a_order', args=[1])
        res = self.client.delete(url)
        self.assertEquals(res.status_code, 204)

    def test_update_order(self):
        url = reverse('orders:a_order', args=[1])
        data = {
            "quantity": 100
        }
        res = self.client.put(url, data=data, format='json')
        self.assertEquals(res.status_code, 200)

    def test_acknowledged_order(self):
        url = reverse('orders:acknowledge_order', args=[1])
        data = {
            "delivery_date": "2023-12-31"
        }
        res = self.client.put(url, data=data, format='json')
        self.assertEquals(res.status_code, 200)

    def test_delivered_order(self):
        url = reverse('orders:acknowledge_order', args=[1])
        data = {
            "delivery_date": "2023-12-31"
        }
        self.client.put(url, data=data, format='json')
        url = reverse('orders:delivered_order', args=[1])
        data = {
            "quality": 5.0
        }
        res = self.client.put(url, data=data, format='json')
        self.assertEquals(res.status_code, 200)





