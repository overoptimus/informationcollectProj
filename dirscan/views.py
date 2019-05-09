from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import dirscan as dirscanutil

# Create your views here.
def dirscan(request):
    return render(request, 'dirscan/dirscan.html')


@csrf_exempt
def startdirscan(request):
    domainName = request.POST.get('domainName')
    file_ext = request.POST.get('file_ext')
    dirscanutil.getUrl(domainName)
    dirscanutil.getFile_EXT(file_ext)
    list = dirscanutil.start()
    # list = [
    #     {
    #         'domainName': domainName,
    #         'file_ext': file_ext
    #     },
    #     {
    #         'id': 2,
    #         'status': 403
    #     }
    # ]
    return JsonResponse({'list': list})
