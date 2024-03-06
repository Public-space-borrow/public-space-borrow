from django.shortcuts import render, redirect
from .models import *
from django.http import Http404, JsonResponse, HttpResponse
from django.core import serializers
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from public_borrow.models import BlackList
# from app import model
import datetime
#新加入的function
def BlackList_print(request):
    # if request.method == "POST":
    #     if request.POST.get("mode") == "blacklist_information":
    #         input_blacklist = black_list(stu_id=request.POST.get('stu_id'), expire_time=request.POST.get('expire_time'), banned_reason=request.POST.get('banned_reason'))
    #         input_blacklist.save()
    
    #         response_html = render(request, "blacklist.html")
    #         response_extra = HttpResponse('黑名單新增成功')
    #         combined_content = response_html.content + response_extra.content
    #         final_response = HttpResponse(combined_content)
    #         return final_response

    # else:
    #     raise Http404("Page not exit")
    return render(request, "blacklist.html")

@csrf_exempt
def BlackList_infor(request):
    if request.method == "POST":
        if request.POST.get("mode") == "blacklist_information":
            # print(request.POST.get('stu_id'))
            # print(request.POST.get('expire_time'))
            # print(request.POST.get('banned_reason'))
            input_blacklist = BlackList(stu_id=request.POST.get('stu_id'), expire_time=request.POST.get('expire_time'), banned_reason=request.POST.get('banned_reason'))
            input_blacklist.save()
    
            return HttpResponse('黑名單新增成功')

    else:
        raise Http404("Page not exit")