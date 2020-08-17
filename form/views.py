from django.shortcuts import render, HttpResponse, redirect, reverse
from . import models as m
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
from django.core.mail import send_mail


def register(request):
    if request.method == "POST":
        cd = request.POST
        if get_user_model().objects.filter(email=cd['email']) or get_user_model().objects.filter(username=cd['full_name']):
            messages.warning(request, 'email or name used before')
            return redirect('register')
        obj = m.Doner()
        obj.user = get_user_model().objects.create_user(username=cd['full_name'])
        obj.user.email = cd['email']
        obj.user.set_password(cd['password'])
        obj.user.save()
        obj.phone = cd['phone']
        obj.address = cd['address']
        obj.blood_type = cd.get("blood_type")
        obj.city = cd.get("city")
        obj.save()
        return HttpResponse('done')

    return render(request, 'form/register.html', {})


def login_user(request):
    cd = request.POST

    if request.method == "POST":
        user = authenticate(request, username=get_user_model().objects.filter(email=cd['email'])[0].username, password=cd['password'])
        if user:
            login(request, user)
            return HttpResponse('done login')
        else:
            messages.warning(request, 'invalid email or password')
            return redirect('login')
    return render(request, 'form/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('home')

import random
def forget_password(request):
    if request.method == "POST":
        email = request.POST['email']
        cod = random.randrange(425713, 905412)
        send_mail('reset password','your reset code is {} don`t share it with anyone else.'.format(code),'mohamed_elsaher2021@gmail.com', [email, ])

        return redirect(reverse('code', args=(cod,)))

    return render(request, 'form/forget.html', {})


def code(request, cod):
    if request.method == "POST":
        if request.POST['code'] == cod:
            return HttpResponse('done done')


