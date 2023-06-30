from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


from .forms import *
from .models import *

menu = [
    {'title': 'Главная', 'urlname': 'home'},
    {'title': 'Программы обучения', 'urlname': 'all'},
    {'title': 'О нас', 'urlname': 'home'},
    {'title': 'Добавить', 'urlname': 'add'},
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
    context['prog'] = prog
    context['p_name'] = p_name
    context['title'] = p_name
    return render(request, 'school/program.html', context=context)

def add(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    context['title'] = 'Добавить'
    context['form'] = form
    return render(request, 'school/add.html', context=context)
