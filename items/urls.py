from django.contrib import admin
from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.itemsSearch, name="itemsSearch"),
    path('<int:pk>/',views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/edit/', views.edit, name="edit"),
]
