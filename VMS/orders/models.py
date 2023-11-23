import uuid

from django.db import models
from vendors.models import Vendor
from django.dispatch import receiver
from django.db.models.signals import pre_save


class PurchaseOrders(models.Model):
    po_number = models.UUIDField(default=uuid.uuid4, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)
    vendor = models.ForeignKey(to=Vendor, to_field='vendor_code', on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, null=True)
    quality = models.FloatField(null=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True)


@receiver(pre_save, sender=PurchaseOrders)
def populate_data(sender, instance, *args, **kwargs):
    instance.quantity = sum(instance.items.values())
