from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

User = get_user_model()

class Tag(models.Model):
    title = models.CharField(max_length=30)
    parent = models.ForeignKey('self',on_delete=CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User ,on_delete=CASCADE,null = False)
    title = models.CharField(max_length=50,null = False)
    describtion = models.CharField(max_length=150,null = False)
    price = models.DecimalField(max_digits=5,decimal_places=2,null = False)
    previous_price = models.DecimalField(max_digits=5,decimal_places=2,null = True,blank=True)
    image = models.ImageField(null = False,upload_to = 'media')
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,null = False)
    describtion = models.CharField(max_length=150,null = False)
    img = models.ImageField(null = False,blank = False,upload_to = 'media')
    is_slider = models.BooleanField(null = True)
    is_discount = models.BooleanField(null = True)
    is_two_blocks = models.BooleanField(null = True)