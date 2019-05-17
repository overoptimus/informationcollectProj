from django.urls import path
from . import views

app_name = 'portscan'
urlpatterns = [
    path('', views.portscan, name='portscanView'),
    path('startportscan/', views.startportscan, name='startportscan'),
]
