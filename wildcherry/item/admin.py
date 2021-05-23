from django.contrib import admin
from django.db import models
from .models import Item,Tag,Event

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','author','title','describtion','price','previous_price','image']
    list_filter = ['id','author','title','price']

class TagAdmin(admin.ModelAdmin):
    list_display = ['title','parent']

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','title','describtion','img','is_slider','is_discount','is_two_blocks']

admin.site.register(Item,ItemAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Event,EventAdmin)