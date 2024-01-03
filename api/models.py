from django.db import models
from django.contrib.auth.models import AbstractUser
from .models import CustomUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name = 'دسته بندی', max_length = 255, blank = True, null = True, default = 'category')
    description = models.TextField(verbose_name = 'توضیحات')

    def __str__(self):
        return self.name
class Membership(models.Model):
    
    first_name = models.CharField(verbose_name ='نام', max_length = 255, blank = True, null = True, default = 'membership')
    last_name = models.CharField(verbose_name ='نام خانوادگی', max_length = 255, blank = True, null = True, default = 'membership')
    email = models.EmailField(verbose_name='ایمیل')
    username = models.CharField(verbose_name='نام کاربری', max_length=255, unique=True)

    def __str__(self):
        return self.username, self.first_name, self.last_name, self.email

class CustomUser(AbstractUser):
    bio = models.CharField(verbose_name = 'بیوگرافی', max_length = 255, blank = True, null = True, default = 'customuser')
    memberships = models.ManyToManyField(Membership)

class Product(models.Model):
    name = models.CharField(verbose_name = 'محصولات', max_length = 255, blank = True, null = True, default = 'product')
    description = models.TextField(verbose_name = 'توضیحات')
    price = models.DecimalField(verbose_name = 'قیمت', max_digits=10, decimal_places=3, blank = True, null = True, default = 'product' )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name, self.price, self.stock_quantity

class Customer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(verbose_name = 'قیمت کل', max_digits=10, decimal_places=3, blank = True, null = True, default = 'order')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(verbose_name = 'جمع کل', max_digits=10, decimal_places=3, blank = True, null = True, default = 'orderitem')
    is_completed = models.BooleanField(default=False)