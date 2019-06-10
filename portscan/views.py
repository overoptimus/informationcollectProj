from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .nmapScan import *
import re
from .models import Port_domain, Port_detail

# Create your views here.


def portscan(request):
    return render(request, 'portscan/portscan.html')


@csrf_exempt
def startportscan(request):
    result = []
    ports_list = []
    network_prefix = request.POST.get('domainName')
    port_range = str(request.POST.get('port_range')).replace("，", " ")
    port_range = port_range.replace(" ", ",")
    ports = port_range.split(',')
    if re.search('-', ports[0]) is not None:
        ports_min = ports[0].split('-')[0]
        ports_max = ports[0].split('-')[1]
        ports_list.extend(str(i) for i in range(int(ports_min), int(ports_max) + 1))
        ports.pop(0)
        for port in ports:
            ports_list.append(port)
    else:
        for port in ports:
            ports_list.append(port)
    # print(ports_list)
    if domain_scaned(network_prefix):
        print(ports_list)
        unscaned_ports = port_unscaned(network_prefix, ports_list)
        db_result = port_search(network_prefix, ports_list)
        result.extend(db_result)
        unscaned_ports_range = ','.join(unscaned_ports)
        if unscaned_ports_range == "":
            return JsonResponse({'result': result})
    else:
        unscaned_ports_range = port_range
    print(port_range)
    print(type(network_prefix))
    print('unscaned ports', unscaned_ports_range)
    p_scan = Portscan(network_prefix, unscaned_ports_range)
    scanning_result = p_scan.startScan()
    result.extend(scanning_result)
    save_db(network_prefix, scanning_result)
    print(result)
    return JsonResponse({'result': result})


# 判断域名是否扫描过
def domain_scaned(domain):
    return Port_domain.objects.isExists(domain)


# 返回未扫描过端口的列表
def port_unscaned(domain, ports_list):
    ports_list_copy = ports_list.copy()
    print('port_unscaned中的ports_list', ports_list)
    port_domain = Port_domain.objects.get(domain=domain)
    scaned_ports = port_domain.port_detail_set.all().values("port")
    for scaned_port in scaned_ports:
        if str(scaned_port['port']) in ports_list_copy:
            ports_list_copy.remove(str(scaned_port['port']))
    return ports_list_copy


# 返回数据库中扫描过端口的信息
def port_search(domain, ports_list):
    print('port_search中的ports_list', ports_list)
    port_domain = Port_domain.objects.get(domain=domain)
    scaned_list = list(
        port_domain.port_detail_set.all().values("port", "status", "reason", "name", "product", "version"))
    for port in scaned_list:
        if str(port["port"]) not in ports_list:
            print(str(port["port"]))
            print(ports_list)
            print('执行remove')
            scaned_list.remove(port)
    return scaned_list


def save_db(domain, result):
    if domain_scaned(domain):
        port_domain = Port_domain.objects.get(domain=domain)
        for port in result:
            port_detail = Port_detail(domain=port_domain, port=port['port'], status=port['status'],
                                      reason=port['reason'], name=port['name'], product=port['product'],
                                      version=port['version'])
            port_detail.save()
    else:
        Port_domain.objects.create(domain=domain)
        port_domain = Port_domain.objects.get(domain=domain)
        for port in result:
            port_detail = Port_detail(domain=port_domain, port=port['port'], status=port['status'],
                                      reason=port['reason'], name=port['name'], product=port['product'],
                                      version=port['version'])
            port_detail.save()
