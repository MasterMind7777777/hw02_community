from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    # В переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию
    # (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # Обозначаем шаблон для этого view.
    template = 'posts/index.html'
    # В словаре context отправляем информацию в шаблон.
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    # В переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе.
    group = get_object_or_404(Group, slug=slug)
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    # Обозначаем шаблон для этого view.
    template = 'posts/group_list.html'
    # Набор переменных передоваемый в шаблон.
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
