from django.contrib import admin
from . models import Userprofile
# Register your models here.
@admin.register(Userprofile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username' , 'email' , 'phone_number')
    search_fields = ('username' , 'email')



#PASSWORD
# MMK
# 1234