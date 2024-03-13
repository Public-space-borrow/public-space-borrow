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
from datetime import datetime
#新加入的function
@csrf_exempt
def BlackList_print(request):

    if request.method == "GET":
        time = BlackList.objects.all().order_by('expire_time').extra(select={'expire_time': "DATE_FORMAT(expire_time, '%%Y%%m%%d')"}).values('stu_id', 'expire_time', 'banned_reason') #.values_list(flat=True)

    time = list(time)

    
    today = datetime.now().strftime('%Y%m%d')
    # print(today)

    data = {
        "time" : time,
        "today" : today,
    }

    # print(data)    

    return render(request, "blacklist.html", data)

@csrf_exempt
def BlackList_input(request):
    if request.method == "POST":
        if request.POST.get("mode") == "blacklist_input":
            # print(request.POST.get('stu_id'))
            # print(request.POST.get('expire_time'))
            # print(request.POST.get('banned_reason'))
            
            if BlackList.objects.filter(stu_id=request.POST.get('stu_id')).exists():
                # error_message = "該學號已存在於黑名單內"
                return HttpResponse('該學號已存在於黑名單內')
            
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

        # original_blacklist = BlackList.objects
        # print(request.POST.get('original_id'))
        # print(request.POST.get('stu_id'))

        edit_blacklist = BlackList.objects.filter(stu_id=request.POST.get('original_id')).update(stu_id=request.POST.get('stu_id'), expire_time=request.POST.get('expire_time'), banned_reason = request.POST.get('banned_reason'))

        # 逐一更新記錄
        # for i in edit_blacklist:
        #     i.stu_id = request.POST.get('stu_id')
        #     i.expire_time = request.POST.get('expire_time')
        #     i.banned_reason = request.POST.get('banned_reason')
        #     i.save()


        # if edit_blacklist:
        #     print(f"Successfully retrieved BlackList record with stu_id: {edit_blacklist.stu_id}")
        # else:
        #     print(f"Failed to retrieve BlackList record with stu_id: {request.POST.get('original_id')}")

        # print(request.POST.get('stu_id'))
        # print(request.POST.get('expire_time'))
        # print(request.POST.get('banned_reason'))

        # edit_blacklist.stu_id = request.POST.get('stu_id')
        # edit_blacklist.expire_time = request.POST.get('expire_time')
        # edit_blacklist.banned_reason = request.POST.get('banned_reason')

        # edit_blacklist.save()

        return HttpResponse('修改成功')
    else:
        return HttpResponse('修改失敗')
    