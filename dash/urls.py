from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard'),
    path('add-request/<int:id>/',views.add_request, name='add_request'),
    path('requests/',views.requests, name='requests'),
    path('accept-request/<int:id>/', views.accept_request, name='accept'),
    path('refuse-request/<int:id>/', views.refuse_request, name='refuse'),



]
