from django.db import models

# Create your models here.

class Userprofile(models.Model):
    username = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200 )
    password = models.CharField(max_length = 15)
    phone_number = models.CharField(max_length = 200)

    def __str__(self):
        return f"{self.username} - {self.email}"

class Book(models.Model):
    book_id = models.IntegerField(unique = True)
    description = models.TextField()
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=255)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)  
    category = models.CharField(max_length=100)
    image_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(Userprofile,on_delete = models.CASCADE,related_name = 'cart')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.book.name} x {self.quantity}"


