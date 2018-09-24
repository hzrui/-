from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import View

from db.base_view import BaseVerifyView
from sup_uesr.forms import RegisterForm, LoginForm
from sup_uesr.helper import login
from sup_uesr.models import Users


class RegisterView(View):
    # 注册功能
    def get(self, request):
        form = RegisterForm()
        return render(request, "reg.html", {'form': form})

    def post(self, request):
        session_code = request.session.get('random_code')
        # 强制转换成
        data = request.POST.dict()
        data['session_code'] = session_code
        # 处理数据
        form = RegisterForm(data)
        if form.is_valid():
            form.save()
            # 注册成功跳转到个人页面
            return redirect(reverse("sup:个人中心"))
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
        context = {
            'phone': phone
        }
        return render(request, "member.html", context)

    def post(self, request):
        pass


class AddressView(BaseVerifyView):
    # 收货地址功能
    def get(self, request):
        pass

    def post(self, request):
        pass


class InfoView(BaseVerifyView):
    # 个人资料功能
    def get(self, request):
        # 验证用户是否登录
        user_id = request.session.get("ID")
        # 查询当前用户的所有信息
        user = Users.objects.filter(pk=user_id).first()

        context = {
            "user": user
        }
        return render(request, "infor.html", context)

    def post(self, request):
        id = request.session.get('ID')
        data = request.POST
        file = request.FILES['head']
        user = Users.objects.get(pk=id)
        user.head = file
        user.save()
        # return HttpResponse('ok')
        return redirect(reverse('sup:个人中心'))


class LogoutView(View):
    # 退出功能
    def get(self, request):
        pass

    def post(self, request):
        pass


@login
def info(request):
    return render(request, 'infor.html')


# 发送验证码
class SendCodeView(View):
    def post(self, request):
        # 接收数据(电话号码)
        phone = request.POST.get('tel', '')
        # 处理数据(手机号码格式判断 正则判断)
        import re
        phone_re = re.compile('^1[3-9]\d{9}$')
        # 匹配手机号字符串
        res = re.search(phone_re, phone)
        if res is None:
            return JsonResponse({'status': '400', 'msg': '手机号码格式错误'})
        res = Users.objects.filter(phone=phone).exists()
        if res:
            return JsonResponse({'status': '400', 'msg': '手机号码已注册'})

        # 生成随机验证码
        import random
        random_code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        # print(random_code)
        # 发送验证码
        print('====={}====='.format(random_code))
        # 将生产的随机码保存到session中
        request.session['random_code'] = random_code
        request.session.set_expiry(60)

        # 响应 json ,告知ajax是否发送成功
        return JsonResponse({'status': '200'})
