from django.shortcuts import render, redirect
from form.models import Doner
from .models import Request
from django.contrib import messages
# Create your views here.


def index(request):
    doners = [x for x in Doner.objects.all() if x.user != request.user ]
    requesting = Doner.objects.get(user=request.user)
    return render(request, 'dash/index.html', {'doners': doners, 'requesting': requesting})


def add_request(request, id):

    r = Request(doner=Doner.objects.get(id=id), user=Doner.objects.get(user=request.user))
    r.save()
    messages.success(request, 'request in queue')
    return redirect('dashboard')


