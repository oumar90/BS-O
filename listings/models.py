from django.db import models
from datetime import datetime
from Core.models import User
# Create your models here.
class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    category = models.CharField(max_length = 150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length = 150)
    state = models.CharField(max_length = 150)
    zipcode = models.CharField(max_length = 150)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_main1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_main2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_main3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_main4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_main5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_main6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
    
    
    
    
    