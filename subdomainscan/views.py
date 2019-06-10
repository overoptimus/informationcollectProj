from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .subdomain import SubdomainUtil

# Create your views here.
def subdomainscan(request):
    return render(request, 'subdomainscan/subdomainscan.html')

@csrf_exempt
def startsubdomainscan(request):
    domain = request.POST.get('domain')
    # pages = int(request.POST.get('pages'))
    subdomain_util = SubdomainUtil(domain)
    subdomain_util.clean_result()
    # for i in range(10):
    #     if i != 0:
    #         page = 1 + i * 10
    #     else:
    #         page = 1
    #     res = subdomain_util.open_url(page)
    #     targets = subdomain_util.find_all(res)
    #     subdomain_util.deal_targets2(targets)
    #     # print(subdomain_util.get_result())
    #     # print('----------------------------------')
    res = subdomain_util.open_url1()
    targets = subdomain_util.find_all1(res)
    subdomain_util.deal_ul(targets)
    result_list = subdomain_util.get_result()
    return JsonResponse({'list': result_list})