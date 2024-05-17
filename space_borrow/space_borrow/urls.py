from django.contrib import admin
from django.urls import path, include
from public_borrow import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("regist", views.regist_page),
    path("request_regist", views.get_regist),
    path("login", views.admin_mode, name="login"),
    path("AdminModel/", include("administrator.urls")),
    path("logout", LogoutView.as_view(), name="logout"),
]
