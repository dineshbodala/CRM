from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    customers=Customer.objects.all()
    orders=order.objects.all()
    totalcustomers=customers.count()
    totalorders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    context={'customers':customers, 'orders':orders,'totalcustomers':totalcustomers,'delivered':delivered,'totalorders':totalorders,'pending':pending}
    return render(request,'accounts/dashboard.html', context)

def products(request):
    products=product.objects.all()
    return render(request, 'accounts/products.html', {'products':products})

def customer(request, pk_test):
    customer=Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    order_count=orders.count()

    context={'customer':customer, 'orders':orders, 'order_count':order_count}
    return render(request, 'accounts/customer.html', context)


