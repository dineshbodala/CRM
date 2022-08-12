
from sre_constants import CATEGORY
from unicodedata import category
from django.db import models


class Customer(models.Model):
    name=models.CharField(max_length=250, null=True)
    phone=models.CharField(max_length=120, null=True)
    email=models.CharField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name  

class tag(models.Model):
    name=models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return self.name  

class product(models.Model):
    CATEGORY=(('Indoor', 'Indoor'), ('Outdoor','OutDoor'))
    name=models.CharField(max_length=250, null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=250, null=True, choices=CATEGORY)
    description=models.CharField(max_length=250, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    Tag=models.ManyToManyField(tag)

    def __str__(self) -> str:
        return self.name  

class order(models.Model):
    STATUS=(('Pending', 'Pending'),('Delivered', 'Delivered'),('Out For Delivery','Out For Delivery'))
    Customer=models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    Product=models.ForeignKey(product, null=True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,  null=True)
    status=models.CharField(max_length=250, null=True, choices=STATUS)

    def __str__(self) -> str:
        return self.Product.name
    





