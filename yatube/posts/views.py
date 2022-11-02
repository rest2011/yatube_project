from django.shortcuts import render
# posts/views.py
from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader


# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template)


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse('Список постов по группам')

# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse('Список постов по группам')