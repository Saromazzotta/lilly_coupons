from django.db import models

class Coupon(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
