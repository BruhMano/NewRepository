from django.shortcuts import render
from .models import Item,Tag,Event

def index(request):
    first_line_of_items = Item.objects.all()[:6]
    items = Item.objects.all()[6:]
    tags = Tag.objects.all()
    events = Event.objects.all()
    return render(request,'index.html',
        {
        'items': items,
        'tags': tags,
        'first_line_of_items': first_line_of_items,
        'events': events
        })

def category_page(request,category):
    tags = Tag.objects.all()
    all_items = Item.objects.all()
    tag_items = []
    for item in all_items:
        for tag in list(item.tag.all()):
            if tag.title == category:
                tag_items.append(item)
                
    return render(request,'category_page.html',{'items': tag_items,'tags': tags})