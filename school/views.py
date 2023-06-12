from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = [
    {'title': 'Главная', 'urlname': 'home'},
    {'title': 'Программы обучения', 'urlname': 'all'},
    {'title': 'О нас', 'urlname': 'home'},
    {'title': 'Контакты', 'urlname': 'home'},
]

context = {
    'menu': menu,
    'title': 'Главная страница'
}


def index(request):
    context['kolvo'] = 4
    return render(request, 'school/index.html', context=context)

def all_items(request):
    context['kolvo'] = None
    return render(request, 'school/index.html', context=context)

def program(request, num):
    prog = Educations.objects.get(pk=num)
    p_name = PhotoEducations.objects.get(pk=num)
    context['prog'] = prog
    context['p_name'] = p_name
    return render(request, 'school/program.html', context=context)
