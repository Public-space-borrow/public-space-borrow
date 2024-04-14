from django.shortcuts import render
from .models import *
from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from public_borrow.models import BlackList

import datetime
from datetime import datetime
from .forms import StudentID
from multiprocessing import Process, Manager
@csrf_exempt
def AdminModel_print(request):
    return render(request, "AdminModel.html")

@csrf_exempt
def BlackList_print(request):
    today = datetime.now().date()
    if request.method == "GET":
        time = BlackList.objects.filter(expire_time__gte=today).order_by('expire_time').extra(select={'expire_time': "DATE_FORMAT(expire_time, '%%Y-%%m-%%d')"}).values('stu_id', 'expire_time', 'banned_reason') #.values_list(flat=True)
    
    data = {
        "time" : time,
        "today" : today,
    }

    return render(request, "blacklist.html", data)

@csrf_exempt
def BlackList_input(request):
    if request.method == "POST":
        if request.POST.get("mode") == "blacklist_input":
            
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

        delete_blacklist = BlackList.objects.get(stu_id=request.POST.get('stu_id'))
        delete_blacklist.delete()

        return HttpResponse('已刪除該筆資料')
    else:
        return HttpResponse('刪除失敗')


@csrf_exempt
def BlackList_edit(request):
    if request.POST.get("mode") == "blacklist_edit":

        BlackList.objects.filter(stu_id=request.POST.get('original_id')).update(stu_id=request.POST.get('stu_id'), expire_time=request.POST.get('expire_time'), banned_reason = request.POST.get('banned_reason'))
        # edit_blacklist = BlackList.objects.filter(stu_id=request.POST.get('original_id')).update(stu_id=request.POST.get('stu_id'), expire_time=request.POST.get('expire_time'), banned_reason = request.POST.get('banned_reason'))


        return HttpResponse('修改成功')
    else:
        return HttpResponse('修改失敗')
    
from .utility import crawl_student

def stu_info(request):
    if request.session['identity'] == "private" and request.method == "POST":
        #adding new ids
        if request.POST.get("ids"): 
            global m
            global student
            global lock
            m = Manager()
            student = m.list()
            form = StudentID(request.POST)
            if form.is_valid():
                ids = form.cleaned_data['ids']
                ids = ids.split()
            data = {
                "total_ids" : len(ids),
            }
            #avoid race condition
            lock = m.Lock()
            global p
            p = Process(target=crawl_student, args=(student, ids, lock))
            p.start()
            return render(request, "show_StudentInfo.html", data)
        #checking proccess status
        elif request.POST.get("check"):
            lock.acquire()
            num_id = len(student)
            lock.release()
            if num_id > 0 and student[-1] == "error":
                return HttpResponse(student[-1])
            return HttpResponse(num_id)
        elif request.POST.get("finish"):
            student_list = list(student)
            del student
            del lock
            del m
            del p
            return JsonResponse(student_list, safe=False)
        elif request.POST.get("shutdown"):
            if p:
                del p
                p.terminate()
            error_message = student[-1]
            del student
            del lock
            del m
            
            return HttpResponse(error_message)
    else:
        raise Http404("Page not found!")
    