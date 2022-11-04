from django.shortcuts import render, get_object_or_404
# posts/views.py
from .models import Post, Group


# Главная страница
def index(request):
    template = 'posts/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Последние обновления на сайте'
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
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    # Словарь с данными принято называть context
    context = {
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Здесь будет информация о группах проекта Yatube',
        'group': group,
        'posts': posts,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)
