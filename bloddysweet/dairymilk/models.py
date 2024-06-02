from django.db import models

class Product(models.Model):
        pro_image=models.TextField(max_length=200)
        pro_name=models.TextField(max_length=200)
        pro_price=models.TextField(max_length=200)
        def __str__(self):
            return self.pro_name
class Contact(models.Model):
        name=models.TextField(max_length=200)
        email=models.CharField(max_length=200)
        phone=models.CharField(max_length=200)
        message=models.TextField(max_length=200)
        def __str__(self):
            return self.name


