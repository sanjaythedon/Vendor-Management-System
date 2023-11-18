from django.db import models
from vendors.models import Vendor


class PurchaseOrders(models.Model):
    po_number = models.CharField(unique=True, max_length=20)
    order_date = models.DateTimeField()
    vendor = models.ForeignKey(to=Vendor, to_field='vendor_code', on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()
