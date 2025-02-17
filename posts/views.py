from django.contrib.admin.templatetags.admin_list import paginator_number
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from posts.models import Post
from .forms import PostCreatModel


# Create your views here.

def index(request):
    posts = Post.published.all()
    q = request.GET.get('q')
    if q and q != "None":
        posts = posts.filter(title__icontains=q) | posts.filter(body__icontains=q)
        # return render(request, 'post/list.html', {
        #     'posts': posts,
        #     'q': q
        # })
    #  pagination  start
    paginator = Paginator(posts, 5)  # paginationga limit berilvot
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)  # postni bolib chiqvotdi shu yerda

    # page = request.GET.get('page')
    # print(page)

    return render(request, 'post/list.html', {
        'q': q,
        'posts': posts

    })


def detail(request, id):
    post = Post.published.filter(id=id).first()
    return render(request, 'post/detail.html', {'post': post})


def create_view(request):
    if request.method == "POST":
        form = PostCreatModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:index")

    else:
        form = PostCreatModel()

    return render(request, 'post/create.html', context={'forms': form})


def edit_view(request, id):
    if request.method == "POST":
        posts = Post.published.get(id=id)
        form = PostCreatModel(request.POST, instance=posts)
        if form.is_valid():
            form.save()
            return redirect("posts:index")
        return render(request, 'post/edit.html', context={
            'form': form,
            'posts': posts

        })
    posts = Post.published.get(id=id)
    form = PostCreatModel(instance=posts)
    return render(request, 'post/edit.html', context={
        'form': form,
        'posts': posts
    })


def delete_view(request, id):
    Post.published.delete(id=id)
    return redirect("posts:index")
