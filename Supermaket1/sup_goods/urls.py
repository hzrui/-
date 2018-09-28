from django.conf.urls import url

from sup_goods.views import IndexView, CategoryView, DetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='首页'),
    url(r'^category/(?P<cate_id>\d+)_(?P<order>\d)/$', CategoryView.as_view(), name='列表'),
    url(r'^detail/(?P<sku_id>\d+)/$', DetailView.as_view(), name='详情'),
]
