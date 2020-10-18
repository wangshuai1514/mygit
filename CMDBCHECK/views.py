from django.shortcuts import render,HttpResponse
from CMDB.settings import commands,scanhosts
from .utils import get_active_hosts,is_ssh_up,login_ssh_passwd
from .models import Server,User
# Create your views here.
def do_scanhots(request):
    for net_host in scanhosts:
        active_hosts = get_active_hosts(net_host)
        for host in active_hosts:
            if is_ssh_up(host):
                server = Server(IP=host)
                server.save()
            else:
                pass
    return HttpResponse("扫描完成")
def scanhots(request):
    return HttpResponse('自动化资产扫描')

