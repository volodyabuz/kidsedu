from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *

menu = [
    {'title': 'Главная', 'urlname': 'home'},
    {'title': 'Программы обучения', 'urlname': 'all'},
    {'title': 'О нас', 'urlname': 'home'},
    {'title': 'Контакты', 'urlname': 'home'},
]

context = {
    'menu': menu,
}


def index(request):
    context['kolvo'] = 4
    context['title'] = 'Главная страница'
    return render(request, 'school/index.html', context=context)

def all_items(request):
    context['kolvo'] = None
    context['title'] = 'Все программы'
    return render(request, 'school/index.html', context=context)

def program(request, num):
    prog = Educations.objects.get(slug=num)
    p_name = get_object_or_404(PhotoEducations, slug=num)
    print(prog, p_name)
    context['prog'] = prog
    context['p_name'] = p_name
    context['title'] = p_name
    return render(request, 'school/program.html', context=context)
