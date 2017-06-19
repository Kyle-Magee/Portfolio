from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .form import LoginForm, RegisterForm, EditForm
from .models import User, Trackers
from django.contrib.auth import hashers
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'tracker.html')


def login_page(request):
    context = {
        'form': LoginForm
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = form['email'].data
        password = form['password'].data
        user = User.objects.get(email=email)
        if user is not None:
            login(request, user)
            return redirect(reverse(edit_tracker))

        else:
            pass

    return render(request, template_name='tracker_login.html', context=context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid() and form['password'].data == form['verify_password'].data:
            user = User(email=form['email'].data, username=form['email'].data,
                        password=hashers.make_password(form['password'].data))
            user.save()
            return redirect(reverse(login_page))

    else:
        form = RegisterForm()

    return render(request, template_name='tracker_register.html', context={'form': form})


@login_required()
def edit_tracker(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        try:
            user_tracker = Trackers.objects.get(user=request.user)
            user_tracker.steam_id = form['steam_id'].data
            user_tracker.time_limit = form['time_limit'].data
            user_tracker.reset_user()
        except:
            user_tracker = Trackers(steam_id=form['steam_id'].data, time_limit=form['time_limit'].data,
                                    user=request.user)
    else:
        form = EditForm()
    return render(request, template_name='edit_tracker.html', context={'form': form})
