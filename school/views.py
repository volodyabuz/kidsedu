from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = [
    'Главная',
    'Программы обучения',
    'О нас',
    'Контакты',
]
context = {
    'menu': menu,
    'title': 'Главная страница'
}

def index(request):
    progs = PhotoEducations.objects.filter(pk__lte=4)
    context['clist'] = progs
    for i in progs:
        print(i)
    return render(request, 'school/index.html', context=context)


def program(request, num):
    progs = Educations.objects.filter(pk=num)
    context['prog'] = prog
    return render(request, 'school/program.html', context=context)