from django.shortcuts import render, redirect
from .models import *
from django.http import Http404, JsonResponse, HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from public_borrow.models import BlackList
import datetime
from datetime import datetime
from .forms import StudentID
@csrf_exempt
def AdminModel_print(request):
    if request.user.is_authenticated and request.user.is_admin == True:
        print("in!@!")
        return render(request, "AdminModel.html")
    else:
        return redirect("home")

@csrf_exempt
def BlackList_print(request):
    today = datetime.now().date()

    # print black list
    if request.method == "GET":
        time = BlackList.objects.filter(expire_time__gte=today).order_by('expire_time').extra(
            select={'expire_time': "DATE_FORMAT(expire_time, '%%Y-%%m-%%d')",
                    'creation_date': "DATE_FORMAT(creation_date, '%%Y-%%m-%%d')"}
        ).values('stu_id', 'expire_time', 'creation_date', 'banned_reason')
    
        data = {
            "time" : time,
            "today" : today,
        }

        return render(request, "blacklist.html", data)

    # add/delete/edit
    if request.method == "POST":

        # ADD black list
        if request.POST.get("mode") == "blacklist_input":
            
            if BlackList.objects.filter(stu_id=request.POST.get('stu_id')).exists():
                return HttpResponse('該學號已存在於黑名單內')
            
            input_blacklist = BlackList(stu_id=request.POST.get('stu_id'), expire_time=request.POST.get('expire_time'), banned_reason=request.POST.get('banned_reason'), creation_date=request.POST.get('creation_date'))
            input_blacklist.save()
    
            return HttpResponse('黑名單新增成功')
        
        # DELETE black list
        elif request.POST.get("mode") == "blacklist_delete":

            delete_blacklist = BlackList.objects.get(stu_id=request.POST.get('stu_id'))
            delete_blacklist.delete()

            return HttpResponse('已刪除該筆資料')

        # EDIT black list
        elif request.POST.get("mode") == "blacklist_edit":

            BlackList.objects.filter(stu_id=request.POST.get('original_id')).update(stu_id=request.POST.get('stu_id'), expire_time=request.POST.get('expire_time'), banned_reason = request.POST.get('banned_reason'))
            return HttpResponse('修改成功')
        
        else:
            return HttpResponse('此動作失敗')

    else:
        raise Http404("Page not exit")

    
from random import random
import uwsgi
def stu_info(request):
    if request.user.is_admin and request.method == "POST":
        #adding new ids
        if request.POST.get("ids"): 
            form = StudentID(request.POST)
            if form.is_valid():
                ids = form.cleaned_data['ids']
                
            r_id = str(int(random() * 1000))
            data = {
                "total_ids" : len(ids.split()),
                "request_id": r_id,
            }
            uwsgi.spool({b"request_id": bytes(r_id, "utf8"), b"ids":bytes(ids, "utf8")})
            return render(request, "show_StudentInfo.html", data)
        #checking proccess status
        elif request.POST.get("check") and request.POST.get("request_id"):
            r_id = request.POST.get("request_id")
            if uwsgi.cache_exists(r_id, "stu_process") != True:
                print(uwsgi.cache_get("error_msg", "stu_process"))
                return HttpResponse("error")
            num_id = uwsgi.cache_get(r_id, "stu_process").decode("utf8")
            if uwsgi.cache_exists("error_msg", "stu_process"):
                print(uwsgi.cache_get("error_msg", "stu_process"))
            print(num_id)
            return HttpResponse(num_id)
        elif request.POST.get("finish") and request.POST.get("request_id"):
            r_id = request.POST.get("request_id")
            if uwsgi.cache_exists(r_id, "stu_process") != True:
                return HttpResponse("error")
            student_list = studentINFO.objects.filter(request_id=r_id).values("stu_id", "email", "name", "department", "phone")
            student_list = list(student_list)
            print(student_list)
            uwsgi.cache_del(r_id, "stu_process")
            return JsonResponse(student_list, safe=False)
        elif request.POST.get("shutdown") and request.POST.get("request_id"):
            uwsgi.cache_update(r_id, b"shutdown", 60000, "stu_process")
            return HttpResponse()
    else:
        raise Http404("Page not found!")
    

from django.db import connection
def admin_reserve(request):
    if request.user.is_authenticated and request.user.is_admin:
        today = datetime.today()
        data = {
            "today" : today
        }
        return render(request, "admin_reserve.html", data)
    else:
        redirect("home")
