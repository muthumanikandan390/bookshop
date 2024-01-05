from django.contrib import admin
from . models import Userprofile , Book, Cart, CartItem
# Register your models here.
@admin.register(Userprofile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username' , 'email' , 'phone_number')
    search_fields = ('username' , 'email')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'price', 'category')
    search_fields = ('name', 'author', 'category')
    list_filter = ('author', 'category')

# Registration for the Cart model
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('created_at',)

# Registration for the CartItem model
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'book', 'quantity')
    search_fields = ('cart__user__username', 'book__name')
    list_filter = ('book',)

#PASSWORD
# MMK
# 1234