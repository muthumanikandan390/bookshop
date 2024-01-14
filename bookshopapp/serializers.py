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
    book = BookSerializer()
    subtotal_count = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['id','cart_id','book_id','quantity','book','subtotal_count']
    
    def get_subtotal_count(self,obj):
        return obj.quantity * obj.book.price


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ['id','created_at','user_id','items','total_price']
    def get_total_price(self,obj):
        total = 0
        for item in obj.items.all():
            book_price = item.book.price
            total = total + book_price 
        return total
        
