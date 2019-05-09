from django.shortcuts import render
from django.http import JsonResponse
from .cms2 import gwhatweb
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def cmsdistinguish(request):
    return render(request, 'cmsdistinguish/cmsdistinguish.html')

@csrf_exempt
def startcmsdistinguish(request):
    url = request.POST.get('url')
    print(url)
    g = gwhatweb(url)
    resultList = g.whatweb(maxsize=1000)
    return JsonResponse({'list': resultList})
