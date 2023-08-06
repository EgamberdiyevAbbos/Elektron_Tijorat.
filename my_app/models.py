from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    
        
    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=12)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    desciription = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class Buy(models.Model):
    name = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    time = models.DateTimeField(auto_now=True) 
    phone = models.IntegerField(max_length=12)
    adress = models.CharField(max_length=100, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
      
    def __str__(self):
        return self.name