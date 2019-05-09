from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request):
    return render(request, 'collectApp/index.html')

def index1(request):
    return redirect('collectApp:index')

def home(request):
    return render(request, 'collectApp/home.html')

def about(request):
    return render(request, 'collectApp/about.html')

def listdetail(request):
    return render(request, 'collectApp/listdetail.html')

def cmsdetail(request):
    return render(request, 'collectApp/cmsdetail.html')

def portdetail(request):
    return render(request, 'collectApp/portdetail.html')

def subdomindetail(request):
    return render(request, 'collectApp/subdomindetail.html')

def details(request):
    return render(request, 'collectApp/details.html')
