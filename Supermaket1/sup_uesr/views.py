from django.shortcuts import render, redirect, reverse
from django.views import View

from db.base_view import BaseVerifyView
from sup_uesr.forms import RegisterForm, LoginForm
from sup_uesr.helper import login


class RegisterView(View):
    # 注册功能
    def get(self, request):
        form = RegisterForm()
        return render(request, "reg.html", {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # 注册成功跳转到个人页面
            return render(request, 'member.html')
        # 失败回到注册页面
        return render(request, 'reg.html', {'form': form})


class LoginView(View):
    # 登录功能
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            # 验证成功保存登录标识
            user = form.cleaned_data.get('user')
            request.session['ID'] = user.pk
            request.session['phone'] = user.phone
            # 设置有效期(关闭浏览器就重新登录)
            request.session.set_expiry(0)

            # 跳转到用户中心
            return redirect(reverse('sup:个人中心'))
        return render(request, 'login.html', {'form': form})


class MemberView(BaseVerifyView):
    # 个人中心功能
    def get(self, request):
        phone = request.session.get('phone')
        return render(request, "member.html", {'phone': phone})

    def post(self, request):
        pass


class AddressView(View):
    # 收货地址功能
    def get(self, request):
        pass

    def post(self, request):
        pass


class InfoView(View):
    # 个人资料功能
    def get(self, request):
        user_di = request.session.get('ID')
        # 没有登录
        if user_di is None:
            return redirect(reverse('sup:登录'))
        return render(request, "infor.html")

    def post(self, request):
        pass


class LogoutView(View):
    # 退出功能
    def get(self, request):
        pass

    def post(self, request):
        pass


@login
def info(request):
    return render(request, 'infor.html')
