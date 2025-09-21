from django.contrib import admin
from .models import Time , Clint , Product , Market
# Register your models here.
class admin_Products(admin.ModelAdmin):
    list_display = ['id','name','price','cotegory','active','product_time']
    list_editable = ['name','price','cotegory','active','product_time']
    list_display_links = ['id']

class admin_Time(admin.ModelAdmin):
    list_display = ['Date','time','moment']
    list_editable = ['time','moment']
    list_display_links = ['Date']

class admin_Clint(admin.ModelAdmin):
    list_display = ['id','name','password','phone']
    list_editable = ['name','password','phone']
    list_display_links = ['id']

class admin_Market(admin.ModelAdmin):
    list_display = ['id','name','place']
    list_editable = ['name','place']
    list_display_links = ['id']
    
admin.site.register(Product , admin_Products)
admin.site.register(Time , admin_Time)
admin.site.register(Clint , admin_Clint)
admin.site.register(Market,admin_Market)

admin.site.site_header = 'wed site management'
admin.site.site_title = 'products management'