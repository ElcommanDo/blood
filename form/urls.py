from django.urls import path
from . import views

urlpatterns = [
    path('registeration-donation/', views.register, name='register'),
    path('login-donation/', views.login_user, name='login'),
    path('logout-donation/', views.logout, name='logout'),
    path('forget-password/', views.forget_password, name='forget'),




]
