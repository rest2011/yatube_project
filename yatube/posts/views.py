from django.shortcuts import render, get_object_or_404
# posts/views.py
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    posts = Post.objects.all()[:10]
    # Словарь с данными принято называть context
    context = {
        'posts': posts,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


# Страница со списком мороженого
def group_posts(request, slug):
    template = 'posts/group_list.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    # Словарь с данными принято называть context
    context = {
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'group': group,
        'posts': posts,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)
