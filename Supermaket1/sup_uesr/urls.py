"""Supermaket1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from sup_uesr.views import RegisterView, LoginView, MemberView

urlpatterns = [
    url(r'^reg/$', RegisterView.as_view(), name="注册"),  # 注册
    url(r'^login/$', LoginView.as_view(), name="登录"),  # 登录
    url(r'^member/$', MemberView.as_view(), name="个人中心"),  # 个人中心
    # url(r'^address/$', AddressView.as_view(), name="address"),  # 收货地址
    # url(r'^info/$', InfoView.as_view(), name="info"),  # 个人资料
    # url(r'^logout/$', LogoutView.as_view(), name="logout"),  # 退出
]
