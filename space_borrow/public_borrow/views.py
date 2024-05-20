from django.shortcuts import render, redirect
from .models import *
from django.http import Http404, JsonResponse, HttpResponse
from django.core import serializers
from django.db import connection
from .utility import check_sequence
from django.views.decorators.csrf import csrf_exempt
import datetime
# Create your views here.
def home(request):
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
        date_to_int = {
            "一" : 0,
            "二" : 1,
            "三" : 2,
            "四" : 3,
            "五" : 4,
            "六" : 5,
            "日" : 6
        }
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
        
        now_datetime = datetime.datetime.now()
        day_diff = date_to_int[record['date']] - now_datetime.weekday() #預約的是禮拜幾 - 現在禮拜幾 = 相差天數
        print(day_diff)
        record['date'] = now_datetime.date() + datetime.timedelta(day_diff)

        if day_diff < 0 or (day_diff == 0 and record['start_time'] < now_datetime.hour):
            return HttpResponse("此時段已不可被修改")
        record['signature'] = str(record['start_time']) + str(request.POST.get('Space_id')) + record['date'].strftime("%Y-%m-%d")
        
        
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
        today = datetime.date.today().isocalendar()
        week_firstDay = datetime.date.fromisocalendar(today.year, today.week, 1)
        all_regist = Register.objects.filter(space=space, date__gte=week_firstDay).values("start_time", "space_id", "date", "user_id", "user_name", "user_phone", "user_dormnumber", "usable")
        all_regist = list(all_regist)
        int_to_date = ['一', '二', '三', '四', '五', '六', '日']
        for record in all_regist:
            if request.user.is_authenticated != True and record["usable"] == 1:
                record['user_id'] = record['user_id'][:-5] + "XXXXX"
                record['user_name'] = record['user_name'][0] + "X" + record['user_name'][2:]
                record['user_phone'] = ""
            record['date'] = int_to_date[record['date'].weekday()]
        return JsonResponse(all_regist, safe=False)
    else:
        raise Http404("Page not exit")

from .form import loginForm
from django.contrib.auth import login, authenticate
def admin_mode(request):
    msg = None
    if request.user.is_authenticated:
        redirect("home")
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user = authenticate(username=username, password=pwd)
            if user:
                login(request, user)
                print("login success")
                return redirect("home")
            else:
                msg = "帳號或密碼錯誤"
        else:
            print(form)
            raise Http404("form invalid!")
    return render(request, "login.html", {"msg": msg})