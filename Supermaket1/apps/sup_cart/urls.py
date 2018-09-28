from django.conf.urls import url

from sup_cart.views import CartAddView, CartDelView, CarShowView

urlpatterns = [
    url(r'^addCar/', CartAddView.as_view(), name="添加购物车"),
    url(r'^delCar/', CartDelView.as_view(), name="减少购物车"),
    url(r'^car/', CarShowView.as_view(), name="购物车"),

]
