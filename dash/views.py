from django.shortcuts import render
from form.models import Doner
# Create your views here.


def index(request):
    doners = Doner.objects.all()
    return render(request, 'dash/index.html', {'doners': doners})
