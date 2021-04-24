from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','author','title','describtion','price','image']
    list_filter = ['id','author','title','price']

admin.site.register(Item,ItemAdmin)