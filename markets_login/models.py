from django.db import models

# Create your models here.

class Market_login (models.Model):
    market_name = models.CharField(max_length = 100)
    branch = [
        ('birleen','birleen'),
        ('cairo','cairo'),
        ('changahi','changahi'),
        ('aslamboom','aslambool'),
    ]
    place = models.CharField(max_length = 100,verbose_name = 'market place',choices = branch)