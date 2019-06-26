from django.shortcuts import render
from django.http import JsonResponse
from .cms2 import gwhatweb
from django.views.decorators.csrf import csrf_exempt
from .models import Cms

# Create your views here.
def cmsdistinguish(request):
    return render(request, 'cmsdistinguish/cmsdistinguish.html')

@csrf_exempt
def startcmsdistinguish(request):
    url = request.POST.get('url')
    print(url)
    if Cms.objects.isExists(url):
        cms = Cms.objects.get(domain=url)
        result_list = [{'cms': cms.cmstype}]
    else:
        g = gwhatweb(url)
        result_list = g.whatweb(maxsize=1000)
        print(result_list)
        if len(result_list) == 0:
            result_list.append({'cms': '未识别'})
        cms = Cms(domain=url, cmstype=result_list[0]['cms'])
        cms.save()
    return JsonResponse({'list': result_list})
