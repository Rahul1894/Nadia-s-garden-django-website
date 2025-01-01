from django.contrib import admin
from .models import Size,Pizza
# Register your models here.
class sizeadmin(admin.ModelAdmin):
    list_display=['title']

class pizzaadmin(admin.ModelAdmin):
    list_display=['topping1','topping2','size']

admin.site.register(Size,sizeadmin)
admin.site.register(Pizza,pizzaadmin)