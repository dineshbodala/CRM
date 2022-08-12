from django.contrib import admin
from .models  import Customer
from .models  import product
from .models import order, tag

admin.site.register(Customer)
admin.site.register(product)
admin.site.register(order)
admin.site.register(tag)
# Register your models here.
