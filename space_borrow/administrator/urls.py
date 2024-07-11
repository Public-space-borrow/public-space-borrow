from django.urls import path
from . import views
urlpatterns = [
    path("", views.AdminModel_print, name="AdminModel"),
    path("blackList", views.BlackList_print, name="black_print"),
    path("stu_info", views.stu_info, name="std_info"),
    path("admin_reserve/", views.admin_reserve, name="admin_reserve"),
    path("add_del_space", views.add_del_space, name="add_del_space"),
]