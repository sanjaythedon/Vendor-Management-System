from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=20)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.name