from django.urls import path
from . import views

app_name = 'cmsdistinguish'
urlpatterns = [
    path('', views.cmsdistinguish, name='cmsdistinguishview'),
    path('startcmsdistinguish/', views.startcmsdistinguish, name='startcmsdistinguish'),
]
