from django.shortcuts import render
# posts/views.py
from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader
# Импортируем модель, чтобы обратиться к ней
from .models import Post


# Главная страница
def index(request):
    template = 'posts/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Это главная страница проекта Yatube',
        'posts': posts,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


# Страница со списком мороженого
def group_posts(request, slug):
    template = 'posts/group_list.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Здесь будет информация о группах проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)
