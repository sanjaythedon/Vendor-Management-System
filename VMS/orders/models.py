import uuid


from django.db import models
from vendors.models import (Vendor,
                            PerformanceHistory)
from django.dispatch import receiver
from django.db.models.signals import (pre_save,
                                      post_save)
from datetime import datetime
from orders.signals import UpdateSignalSender


class PurchaseOrders(models.Model):
    po_number = models.CharField(unique=True, max_length=20)
    order_date = models.DateTimeField()
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
    # print(sender)
    print(kwargs)
    # print(instance.acknowledgment_date)
    print("Populate data running")
    instance.quantity = sum(instance.items.values())


@receiver(pre_save, sender=PurchaseOrders)
def set_response_time(sender, instance, *args, **kwargs):
    print(f"PRE SAVE")
    a = kwargs['update_fields']
    print(a)

    if a and 'acknowledgment_date' in a:
        print("Successful")
        vendor = str(instance.vendor)
        print(f"Vendor ID = {vendor}")
        no_of_orders = PurchaseOrders.objects.filter(vendor=vendor, acknowledgment_date__isnull=False).count()
        print(f"Number of orders for the vendor: {no_of_orders}")
        issue_date = instance.issue_date.replace(tzinfo=None)
        acknowledgment_date = instance.acknowledgment_date
        print(f"{issue_date=}")
        print(f"{acknowledgment_date=}")
        # current_qra = Vendor.objects.all().values('vendor_code')
        # current_art = Vendor.objects.filter(vendor_code=vendor).update(average_response_time=80.0)
        # print("Average response time updated")
        current_art = Vendor.objects.filter(vendor_code=vendor)
        print(current_art)
        for i in current_art:
            # print(i.average_response_time)
            print(f"{i.average_response_time=}")
            num1 = i.average_response_time * no_of_orders
            num2 = (acknowledgment_date - issue_date).seconds / 60
            art = (num1 + num2) / (no_of_orders + 1)
            print(f"{num2=}")
            print(f"{art=}")
        q = current_art.update(average_response_time=art)
        print(q)


@receiver(pre_save, sender=PurchaseOrders)
def set_quality_rating_avg(instance, *args, **kwargs):
    if instance.status == 'completed':
        vendor_id = str(instance.vendor)
        purchase_order = PurchaseOrders.objects.all()
        po = purchase_order.filter(vendor=vendor_id, status='completed')
        no_of_orders = po.count()
        vendor = Vendor.objects.get(vendor_code=vendor_id)
        current_qra = vendor.quality_rating_avg
        qra_num1 = current_qra * no_of_orders
        qra_num = qra_num1 + instance.quality
        denom = no_of_orders + 1
        qra = qra_num / denom
        vendor.quality_rating_avg = qra
        print("Quality rating average is set")
        print(instance.delivery_date)
        no_of_proper_delivery = 1 if instance.delivery_date >= datetime.now() else 0
        current_ota = vendor.on_time_delivery_rate
        ota_num1 = current_ota * no_of_orders
        ota_num = ota_num1 + no_of_proper_delivery
        ota = ota_num / denom
        vendor.on_time_delivery_rate = ota
        fulfill = 0 if instance.issue_date is None else 1
        fr_orders = purchase_order.filter(vendor=vendor_id, issue_date__isnull=False).count()
        current_fr = vendor.fulfillment_rate
        fr_num1 = current_fr * no_of_orders
        fr_num = fr_num1 + fulfill
        fr = fr_num / fr_orders
        vendor.fulfillment_rate = fr
        vendor.save()

        ph = PerformanceHistory.objects.create(vendor=vendor,
                                               on_time_delivery_rate=ota,
                                               quality_rating_avg=qra,
                                               average_response_time=vendor.average_response_time,
                                               fulfillment_rate=fr)
        print('Entry in performance history is created')















# @receiver(pre_save, sender=PurchaseOrders)
# def set_response_time(sender, instance, *args, **kwargs):
#     print(sender)
#     print(instance)

# @receiver(UpdateSignalSender.acknowledge_update, sender=UpdateSignalSender)
# def set_response_time(*args, **kwargs):
#     print(f"{args=}")
#     print(f"{kwargs=}")

