from django.urls import path
from . import views

app_name='dirscan'
urlpatterns = [
    path('', views.dirscan, name='dirscanView'),
    path('startdirscan/', views.startdirscan, name='startdirscan'),
]
