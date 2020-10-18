from django.shortcuts import render,HttpResponse

# Create your views here.
def scanhots(request):
    return HttpResponse('自动化资产扫描')
