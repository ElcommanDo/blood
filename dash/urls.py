from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard'),
    path('add-request/<int:id>/',views.add_request, name='add_request'),


]
