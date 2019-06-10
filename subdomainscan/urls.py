from django.urls import path
from . import views

app_name = 'subdomainscan'
urlpatterns = [
    path('', views.subdomainscan, name='subdomainscanView'),
    path('startsubdomainscan/', views.startsubdomainscan, name='startsubdomainscan'),
]