from django.shortcuts import render, redirect
from form.models import Doner
from .models import Request
from django.contrib import messages
# Create your views here.


def index(request):
    doners = [x for x in Doner.objects.all() if x.user != request.user ]
    requesting = Doner.objects.get(user=request.user)
    if request.method == "POST":
        blood = request.POST.get("blood_type")
        doners = [x for x in Doner.objects.filter(blood_type=blood) if x.user != request.user]
    return render(request, 'dash/index.html', {'doners': doners, 'requesting': requesting})


def add_request(request, id):

    r = Request(doner=Doner.objects.get(id=id), user=Doner.objects.get(user=request.user))
    r.save()
    messages.success(request, 'request in queue')
    return redirect('dashboard')


def requests(request):
    user = Doner.objects.get(user=request.user)
    recieved_requests = [x for x in Request.objects.filter(doner=user) if x.case is None]
    sent_requests = Request.objects.filter(user=user)
    return render(request, 'dash/req-to.html', {'sent': sent_requests,'rec': recieved_requests})


def accept_request(request,id):
    obj = Request.objects.get(id=id)
    obj.case = True
    obj.save()
    return redirect('requests')


def refuse_request(request,id):
    obj = Request.objects.get(id=id)
    obj.case = False
    obj.save()
    return redirect('requests')


def edit(request):
    return render(request, 'dash/edit.html', {})

