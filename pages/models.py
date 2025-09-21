from django.db import models
from django.utils import timezone

# Create your models here.

class Time (models.Model):
    Date = models.DateField(default=timezone.now)
    time = models.TimeField(null = True)
    moment = models.DateTimeField(null = True)
    # methods
    # def __str__ (self):
    #     if self.moment:
    #         return str(self.moment)
    #     elif self.time:
    #         return f"{self.Date} {self.time}"
    #     else:
    #         return str(self.Date)
    class Meta :
        verbose_name = 'time'
        ordering = ['-moment']


class Product (models.Model):
    # attridutes
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length = 100,default = 'enter name')
    price=models.DecimalField(max_digits = 6,decimal_places=2,default = 0.0)
    image= models.ImageField(upload_to = 'photos/%y/%m/%d',default = 'photos/25/09/13/tour-list-4.png')
    content=models.TextField(null= True,blank=True)
    # categories
    categories = [
        ('phone','phone'),
        ('computer','computer'),
        ('TV','TV'),
        ('car','car'),
        ('fan','fan'),
    ]
    cotegory=models.CharField(max_length = 100,verbose_name = 'category',choices = categories)
    active=models.BooleanField(default=True)
    # relation
    product_time = models.OneToOneField(Time ,on_delete=models.CASCADE, null=True, blank=True)
    # methods
    def __str__ (self):
        return self.name
    class Meta : 
        verbose_name = 'product'
        ordering = ['id']

class Clint (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    phone = models.BigIntegerField(default=0)
    image = models.ImageField(upload_to = 'clint_photo/%y/%m/%d',default = 'photos/25/09/13/tour-list-4.png')
    product = models.ManyToManyField(Product)
    def __str__ (self):
        return self.name
    class Meta :
        verbose_name = 'clint'
        ordering = ['-name']

class Market (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100,default = "")
    branch = [
        ('birleen','birleen'),
        ('cairo','cairo'),
        ('changahi','changahi'),
        ('aslamboom','aslambool'),
    ]
    place = models.CharField(max_length = 100,verbose_name = 'market place',choices = branch)
    vesetors = models.ManyToManyField(Clint,blank=True)
    market_products = models.ManyToManyField(Product,blank=True)
