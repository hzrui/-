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
from django.conf.urls import url, include
from django.contrib import admin

from sup_goods.views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #上传部件自动调用上传地址
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # 全文搜索框架
    url(r'^search/', include('haystack.urls')),
    #应用app
    url(r'^sup/', include('sup_uesr.urls',namespace='sup')),
    url(r'^goods/', include('sup_goods.urls', namespace='goods')),
    url(r'^car/', include('sup_cart.urls', namespace='cart')),
    # 商城首页
    url(r'^$', IndexView.as_view(), name='商城首页'),
]
