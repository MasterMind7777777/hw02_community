from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def paginator_my(request, post_list):
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    post_list = Post.objects.all()
    page_obj = paginator_my(request, post_list)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    page_obj = paginator_my(request, post_list)
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    full_name = user.get_full_name()

    post_list = user.posts.all()
    post_count = post_list.count()
    page_obj = paginator_my(request, post_list)

    context = {
        'page_obj': page_obj,
        'post_count': post_count,
        'full_name': full_name,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = get_object_or_404(User, id=post.author.id)

    full_name = user.get_full_name()
    post_count = user.posts.all().count()
    context = {
        'post': post,
        'user': user,
        'full_name': full_name,
        'post_count': post_count,
    }
    return render(request, 'posts/post_detail.html', context)
