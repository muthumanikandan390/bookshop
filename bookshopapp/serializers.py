from rest_framework import serializers
from . models import Book,CartItem,Cart

class BookSerializer(serializers.ModelSerializer):
    truncated_description = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['id', 'book_id', 'description', 'truncated_description', 'name', 'author', 'price', 'currency', 'category', 'image_path']

    def get_truncated_description(self, obj):
        max_length = 100
        if len(obj.description) > max_length:
            return obj.description[:max_length] + '...'
        return obj.description

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id','cart_id','book_id','quantity']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','created_at','user_id']
        
