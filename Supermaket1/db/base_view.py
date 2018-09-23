from django.utils.decorators import method_decorator
from django.views import View

from sup_uesr.helper import login


class BaseVerifyView(View):

    # 登录验证的装饰器
    @method_decorator(login)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)