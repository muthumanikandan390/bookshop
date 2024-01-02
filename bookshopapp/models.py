from django.db import models

# Create your models here.

class Userprofile(models.Model):
    username = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200 )
    password = models.CharField(max_length = 15)
    phone_number = models.CharField(max_length = 200)

    def __str__(self):
        return f"{self.username} - {self.email}"