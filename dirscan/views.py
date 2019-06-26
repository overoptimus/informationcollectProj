from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import dirscan as dirscanutil
from .models import Dir_detail, Dir_domain


# Create your views here.
def dirscan(request):
    return render(request, 'dirscan/dirscan.html')


@csrf_exempt
def startdirscan(request):
    dir_list = []
    domainName = request.POST.get('domainName')
    file_ext = request.POST.get('file_ext')
    if Dir_domain.objects.isExists(domainName=domainName):
        db_domain = Dir_domain.objects.get(domain=domainName)
        db_dir_list = db_domain.dir_detail_set.all()
        for dir_detail in db_dir_list:
            dir_dict = {
                'url': dir_detail.dir,
                'status': dir_detail.status
            }
            dir_list.append(dir_dict)
    else:
        # file_ext = request.POST.get('file_ext')
        dirscanutil.getUrl(domainName)
        dirscanutil.getFile_EXT(file_ext)
        dirscanutil.clean_result()
        dir_list = dirscanutil.start()
        save_dir_list(domainName, file_ext, dir_list)
    return JsonResponse({'list': dir_list})


def save_dir_list(domainName, file_ext, dir_list):
    print(domainName, file_ext, dir_list)
    dir_domain = Dir_domain(domain=domainName, file_ext=file_ext)
    dir_domain.save()
    # Dir_domain.objects.create(domain=domainName, file_ext=file_ext)
    for dir in dir_list:
        print('url:', dir['url'])
        print('status:', dir['status'])
        dir_detail = Dir_detail(domain=dir_domain, dir=dir['url'], status=dir['status'])
        dir_detail.save()