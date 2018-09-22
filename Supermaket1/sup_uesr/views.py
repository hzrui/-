from django.shortcuts import render
from django.views import View


class RegisterView(View):
    # 注册功能
    def get(self, request):
        return render(request, "reg.html")

    def post(self, request):
        pass


class LoginView(View):
    # 登录功能
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        pass


class MemberView(View):
    # 个人中心功能
    def get(self, request):
        return render(request, "member.html")

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
        return render(request, "infor.html")

    def post(self, request):
        pass


class LogoutView(View):
    # 退出功能
    def get(self, request):
        pass

    def post(self, request):
        pass
