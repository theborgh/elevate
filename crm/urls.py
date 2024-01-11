from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('register/', views.register, name='register'),
    path('clients/', views.clients, name='clients'),
]
