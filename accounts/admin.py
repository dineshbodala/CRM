from django.contrib import admin
from .models  import customer
from .models  import product
from .models import order

admin.site.register(customer)
admin.site.register(product)
admin.site.register(order)
# Register your models here.
