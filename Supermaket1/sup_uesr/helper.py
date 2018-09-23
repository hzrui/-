import hashlib

# 密码加密
from django.shortcuts import redirect
from django.urls import reverse

from django.conf import settings


def set_password(pwd):
    token = settings.SECRET_KEY
    password = token + pwd
    h = hashlib.sha1(password.encode('utf-8'))
    return h.hexdigest()


# 登录装饰器
def login(fun):
    def verify_login(request, *args, **kwargs):
        if request.session.get('ID') is None:
            # 没有登录
            return redirect(reverse('sup:登录'))
        else:
            return fun(request, *args, **kwargs)

    return verify_login
