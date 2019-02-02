from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RedditUserCreationForm, AuthForm
from django.contrib.auth import login, logout
from django.contrib import messages


def homepage(request):
    # messages.success(request, 'success')
    # messages.info(request, 'info')
    # messages.warning(request, 'warning')
    # messages.error(request, 'error')
    # messages.debug(request, 'debug')

    return render(request, 'rddt_main/main.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('rddt_main:profile')

    if request.method == 'POST':
        form = RedditUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('rddt_main:profile')
    else:
        form = RedditUserCreationForm()

    return render(request, 'rddt_main/register.html', context={"form": form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('rddt_main:homepage')

    if request.method == 'POST':
        form = AuthForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('rddt_main:homepage')
    else:
        form = AuthForm

    return render(request, 'rddt_main/login.html', context={"form": form})


def logout_page(request):
    logout(request)
    return redirect('rddt_main:homepage')


def profile(request):
    return render(request, 'rddt_main/profile.html')
