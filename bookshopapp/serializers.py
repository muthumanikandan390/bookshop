from rest_framework import serializers
from . models import Book

class BookSerializer(serializers.ModelSerializer):
    truncated_description = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = fields = ['id', 'book_id', 'description', 'truncated_description', 'name', 'author', 'price', 'currency', 'category', 'image_path']

    def get_truncated_description(self, obj):
        max_length = 100
        if len(obj.description) > max_length:
            return obj.description[:max_length] + '...'
        return obj.description