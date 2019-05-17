from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def portscan(request):
    return render(request, 'portscan/portscan.html')


@csrf_exempt
def startportscan(request):
    pass