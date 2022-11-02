from django.shortcuts import render
# ice_cream/views.py
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse('Список постов по группам')
