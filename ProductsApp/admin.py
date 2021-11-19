from django.contrib import admin
from .models import productmodel
# Register your models here.

class productmodeladmin(admin.ModelAdmin):
    list_display = ['name','weight','price','created_at','updated_at']

admin.site.register(productmodel,productmodeladmin)