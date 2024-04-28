"""
URL configuration for space_borrow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from public_borrow import views
from administrator import views as administrator_views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("regist", views.regist_page),
    path("request_regist", views.get_regist),
    path("login", views.admin_mode, name="login"),
    path("AdminModel", administrator_views.AdminModel_print, name="AdminModel"),
    path("blackList", administrator_views.BlackList_print, name="black_print"),
    path("stu_info", administrator_views.stu_info, name="std_info"),
    path("logout", LogoutView.as_view(), name="logout"),
]
