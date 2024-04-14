from django.shortcuts import render
from .models import *
from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from public_borrow.models import BlackList
from django.db.models import F
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
                print("return error")
                return HttpResponse("error")
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
                p.terminate()
                del p
            error_message = student[-1]
            del student
            del lock
            del m
            
            return HttpResponse(error_message)
    else:
        raise Http404("Page not found!")
    