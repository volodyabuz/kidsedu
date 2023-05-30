from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('programma/<int:num>', program, name='programma'),
    path('all', all_items, name='all'),
]
