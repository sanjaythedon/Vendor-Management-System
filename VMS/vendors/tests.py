from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Vendor


class VendorTest(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(name="Kohli",
                                       address="RCB",
                                       contact_details="18")
        # print("\nSet up for test case is done!")

    def test_vendor_list(self):
        url = reverse('vendors:vendorList')
        res = self.client.get(url)
        self.assertEquals(res.status_code, 200)

    def test_vendor_details(self):
        url = reverse('vendors:vendorDetail', args=[1])
        res = self.client.get(url)
        self.assertEquals(res.status_code, 200)

    def test_vendor_performance_metric(self):
        url = reverse('vendors:vendorPerformance', args=[1])
        res = self.client.get(url)
        self.assertEquals(res.status_code, 200)

    def test_performance_metric_history(self):
        url = reverse('vendors:allVendorPerformance')
        res = self.client.get(url)
        self.assertEquals(res.status_code, 200)

    def test_create_vendor(self):
        url = reverse('vendors:vendorList')
        data = {
                    "name": "Virgil",
                    "address": "Paris, France",
                    "contact_details": "1111111"
                }
        res = self.client.post(url, data=data, format='json')
        self.assertEquals(res.status_code, 201)

    def test_update_vendor(self):
        url = reverse('vendors:vendorDetail', args=[1])
        data = {
            "name": "Sanjay",
            "address": "xyz, abc, 123",
            "contact_details": "1234567890"
        }
        res = self.client.put(url, data=data, format='json')
        self.assertEquals(res.status_code, 200)

    def test_delete_vendor(self):
        url = reverse('vendors:vendorDetail', args=[1])
        res = self.client.delete(url)
        self.assertEquals(res.status_code, 204)

