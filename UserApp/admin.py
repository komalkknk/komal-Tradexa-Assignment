from django.contrib import admin
from .models import usermodel,postmodel
# Register your models here.

class usermodelAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','password','username']

class postmodelAdmin(admin.ModelAdmin):
    list_display = ['user','text','created_at','updated_at']

admin.site.register(usermodel,usermodelAdmin)
admin.site.register(postmodel,postmodelAdmin)