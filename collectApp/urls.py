from django.urls import path, include
from . import views

app_name = 'collectApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index1),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('listdetail/', views.listdetail, name='listdetail'),
    path('cmsdetail/', views.cmsdetail, name='cmsdetail'),
    path('portdetail/', views.portdetail, name='portdetail'),
    path('subdomindetail/', views.subdomindetail, name='subdomindetail'),
    path('details/', views.details, name='details'),
]
