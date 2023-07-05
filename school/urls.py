from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('programma/<slug:num>', program, name='programma'),
    path('all', all_items, name='all'),
    path('add_page', add, name='add'),
    path('test', TestPage.as_view(), name='test'),
]
