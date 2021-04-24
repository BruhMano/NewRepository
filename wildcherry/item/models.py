from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

User = get_user_model()


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User ,on_delete=CASCADE,null = False)
    title = models.CharField(max_length=30,null = False)
    describtion = models.CharField(max_length=150,null = False)
    price = models.DecimalField(decimal_places=2,null = False)
    image = models.ImageField(null = False,upload_to = 'media')
