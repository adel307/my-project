from django.contrib import admin
from .models import Time , Clint , Product , Market
# Register your models here.
admin.site.register(Product)
admin.site.register(Time)
admin.site.register(Clint)
admin.site.register(Market)