from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home/index.html'

def contact(request):
    if request.method == "POST":
        cd = request.POST
        send_mail('')
