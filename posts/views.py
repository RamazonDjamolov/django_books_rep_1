from django.shortcuts import render, redirect

from posts.models import Post
from .forms import PostCreatModel


# Create your views here.

def index(request):
    posts = Post.published.all()
    return render(request, 'post/list.html', {'posts': posts})


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
