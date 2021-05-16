from django.urls import path
from .views import index,category_page

urlpatterns = [
    path('', index, name='index'),
    path('category/<str:category>/',category_page,name='category'),
]