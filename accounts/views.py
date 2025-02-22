from os import remove

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from .forms import CreateUserForm, LoginForm


def signup_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.set_password(form.cleaned_data['password'])
            # user.save()
            # print('redirect iwlash kere')
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save(True)
            return redirect('accounts:login')
        return render(request, template_name='accounts/sign_in.html', context={
            'form': form
        })

    form = CreateUserForm()

    return render(request, template_name='accounts/sign_in.html', context={
        'form': form
    })


def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            print(user, "authenticate")
            if user is not None:
                login(request, user)
                return redirect('posts:index')
            form.add_error("", 'username yoki parol xatoo')
        return render(request, template_name='accounts/login.html', context={
            'form': form
        })

    return render(request, template_name='accounts/login.html', context={
        'form': form
    })


def logout_view(request):
        logout(request)
        return redirect('posts:index')