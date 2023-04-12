from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name="contact"),
    path('signUp/', views.signUp, name="signUp"),
    path('user_login/', views.user_login, name="user_login"),
    path('logout_user/', views.logout_user, name="logout_user"),
]
