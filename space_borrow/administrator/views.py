from django.shortcuts import render, redirect
from django.core.serializers import serialize
from .models import *
from django.http import Http404, JsonResponse, HttpResponse
from django.core import serializers
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from public_borrow.models import BlackList
# from app import model
import json
import datetime
from datetime import date
#新加入的function
@csrf_exempt
def BlackList_print(request):

    if request.method == "GET":
        time = BlackList.objects.all().order_by('expire_time').extra(select={'expire_time': "DATE_FORMAT(expire_time, '%%Y%%m%%d')"}).values('stu_id', 'expire_time', 'banned_reason') #.values_list(flat=True)

    time = list(time)

    data = {
        "time" : time,
    }

    print(data)    

    return render(request, "blacklist.html", data)

@csrf_exempt
def BlackList_input(request):
    if request.method == "POST":
        if request.POST.get("mode") == "blacklist_input":
            # print(request.POST.get('stu_id'))
            # print(request.POST.get('expire_time'))
            # print(request.POST.get('banned_reason'))
            input_blacklist = BlackList(stu_id=request.POST.get('stu_id'), expire_time=request.POST.get('expire_time'), banned_reason=request.POST.get('banned_reason'))
            input_blacklist.save()
    
            return HttpResponse('黑名單新增成功')

    else:
        raise Http404("Page not exit")
    

@csrf_exempt
def BlackList_delete(request):
    if request.POST.get("mode") == "blacklist_delete":
        # print(request.POST.get('stu_id'))
        # print(request.POST.get('expire_time'))
        # print(request.POST.get('banned_reason'))
        # input_blacklist = BlackList(stu_id=request.POST.get('stu_id'), expire_time=request.POST.get('expire_time'), banned_reason=request.POST.get('banned_reason'))
        # input_blacklist.save()

        delete_blacklist = BlackList.objects.get(stu_id=request.POST.get('stu_id'))
        delete_blacklist.delete()

        return HttpResponse('已刪除該筆資料')
    else:
        return HttpResponse('刪除失敗')


@csrf_exempt
def BlackList_edit(request):
    if request.POST.get("mode") == "blacklist_edit":
        # print(request.POST.get('stu_id'))
        # print(request.POST.get('expire_time'))
        # print(request.POST.get('banned_reason'))
        # input_blacklist = BlackList(stu_id=request.POST.get('stu_id'), expire_time=request.POST.get('expire_time'), banned_reason=request.POST.get('banned_reason'))
        # input_blacklist.save()

        edit_blacklist = BlackList.objects.get(stu_id=request.POST.get('stu_id'))

        edit_blacklist.stu_id = request.POST.get('stu_id')
        edit_blacklist.expire_time = request.POST.get('expire_time')
        edit_blacklist.banned_reason = request.POST.get('banned_reason')

        edit_blacklist.save()

        return HttpResponse('修改成功')
    else:
        return HttpResponse('修改失敗')
    