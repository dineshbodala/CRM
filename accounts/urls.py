from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customers/<str:pk_test>', views.customer, name='customer'),
    path('createorder/', views.createorder, name='createorder'),
    path('updateorder/<str:pk>', views.updateorder, name='updateorder'),
    path('delete/<str:pk>', views.deleteorder, name='delete'),
]


