from django.shortcuts import render
from .models import *
from django.http import Http404, JsonResponse, HttpResponse
from django.core import serializers
from django.db import connection
from .utility import check_sequence
from django.views.decorators.csrf import csrf_exempt
import datetime
# Create your views here.
def home(request):
    if 'identity' not in request.session:
        request.session['identity'] = "normal"
    wulin = Space.objects.filter(region__exact='武嶺')
    CueiHeng = Space.objects.filter(region__exact='翠亨')
    YuShu = Space.objects.filter(region__exact="雨樹")
    data = {
        "wulin" : wulin,
        "CueiHeng":CueiHeng,
        "YuShu":YuShu,
    }
    return render(request, "main_page.html", data)

def regist_page(request):
    if request.method == "GET":
        space_id = int(request.GET['space_id'])
        region = Space.objects.filter(id__exact=space_id).values_list('region', flat=True).first()
        all_region_space = Space.objects.filter(region=region).values('space_name', 'id')
        data = {
            'region_space' : all_region_space,
        }
        return render(request, "apply.html", data)
    elif request.method == "POST":
        record = {
            'space' : Space.objects.filter(id__exact=request.POST.get('Space_id')).first(),
            'start_time' : request.POST.get('Start_time'),
            'user_id' : request.POST.get('user_id'),
            'user_dormnumber' : request.POST.get('user_dormnumber'),
            'user_phone' : request.POST.get('user_phone'),
            'change_pwd' : request.POST.get('change_pwd'),
            'date' : request.POST.get('date'),
            'user_name' : request.POST.get('name'),
            'usable': 1
        }
        record['start_time'] = int(record['start_time'].split(':')[0])
        record['signature'] = str(record['start_time']) + str(request.POST.get('Space_id')) + record['date']

        date_to_int = {
            "一" : 0,
            "二" : 1,
            "三" : 2,
            "四" : 3,
            "五" : 4,
            "六" : 5,
            "日" : 6
        }
        now_datetime = datetime.datetime.now()
        if date_to_int[record['date']] < now_datetime.weekday() or date_to_int[record['date']] == now_datetime.weekday() and record['start_time'] < now_datetime.hour:
            return HttpResponse("此時段已不可修改")
        if request.POST.get('mode') == "add":
            b_list = BlackList.objects.filter(stu_id__exact=record['user_id']).first()
            if(b_list):
                return HttpResponse(f"此學號已經被列入黑名單\n原因為:{b_list.banned_reason}\n若有疑問請至宿舍服務組洽詢")
            if(len(Register.objects.filter(signature__exact=record['signature']))):
                return HttpResponse("這個時段已經被預約！")
            today_regist = list(Register.objects.filter(date=record['date'], user_id=record['user_id']).values_list('start_time', flat=True))
            today_regist.append(record['start_time'])
            if check_sequence(today_regist):
                return HttpResponse("此空間不可連續預約2小時以上！")
            new_record = Register(**record)
            new_record.save()
            return HttpResponse("預約成功\n使用前請至服務站出示學生證以借用鑰匙")
        elif request.POST.get("mode") == "delete":
            print(record['signature'])
            target_regist = Register.objects.filter(signature=record['signature']).first()
            if(target_regist == None):
                return HttpResponse("該預約資料已經不存在")
            if record['change_pwd'] == target_regist.change_pwd:
                target_regist.delete()
                return HttpResponse("刪除成功！")
            else:
                return HttpResponse("密碼錯誤！")
    else:
        raise Http404("Page not exit")
            

def get_regist(request):
    if request.method == "POST":
        space = request.POST.get('id')
        all_regist = Register.objects.filter(space=space).values("start_time", "space_id", "date", "user_id", "user_name", "user_phone", "user_dormnumber")
        all_regist = list(all_regist)
        if request.session['identity'] == "normal":
            for record in all_regist:
                record['user_id'] = record['user_id'][:-5] + "XXXXX"
                record['user_name'] = record['user_name'][0] + "X" + record['user_name'][2:]
                record['user_phone'] = ""
        return JsonResponse(all_regist, safe=False)
    else:
        raise Http404("Page not exit")
    
@csrf_exempt
def admin_mode(request):
    if request.method == "POST":
        if request.POST.get("mode") == "login":
            if request.POST.get("pwd") == "76211194":
                request.session['identity'] = "private"
                return HttpResponse("登入成功，切換為管理者模式")
            else:
                return HttpResponse("密碼錯誤！")
        else:
            request.session['identity'] = "normal"
            return HttpResponse("登出成功，切換為一般模式")
    else:
        raise Http404("Page not exit")