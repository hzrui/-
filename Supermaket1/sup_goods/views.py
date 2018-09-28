from django.shortcuts import render, redirect, reverse
from django.views import View

# 首页
from django_redis import get_redis_connection

from db.base_view import BaseVerifyView
from sup_cart.helper import get_car_key
from sup_goods.models import GoodsSKU, Banner, Category, ActivityZone


class IndexView(View):
    def get(self, request):
        # 接收
        activs = ActivityZone.objects.filter(is_delete=False)
        banner = Banner.objects.filter()
        context = {
            'goods_sku': banner,
            'activs': activs
        }
        return render(request, 'sup_goods/index.html', context)

    def post(self, request):
        pass


# 列表
class CategoryView(View):
    def get(self, request, cate_id=0, order=0):
        cate_id = int(cate_id)
        order = int(order)
        # 查询所有的分类,进行显示
        categorys = Category.objects.filter(is_delete=False)
        # 获取对应分类想的商品
        if cate_id == 0:
            # 默认展示第一个分类下的商品
            category = categorys.first()
            # 如果cate_id=0,cate_id就应该为分类的id
            cate_id = category.pk
        else:
            category = Category.objects.get(pk=cate_id)

        # sku商品
        # goods_skus = GoodsSKU.objects.filter(is_delete=False)
        # 对应分类商品(映射关系)
        order_by_rule = ['id', '-sale_num', '-price', 'price', 'create_time']
        goods_skus = category.goodssku_set.all().order_by(order_by_rule[order])


        #获取该用户购物车中商品的总数
        user_id = request.session.get('ID',None)
        total = 0
        if user_id:
            cnn = get_redis_connection('default')
            #准备购物车的键
            car_key = 'car_%s' % user_id
            car_values = cnn.hvals(car_key)

            for v in car_values:
                # print(v)
                total += int(v)



        # 组装一个字典
        context = {
            'goods_skus': goods_skus,
            'categorys': categorys,
            'cate_id': cate_id,
            'order': order,
            'total': total,
        }
        return render(request, 'sup_goods/category.html', context)

    def post(self, request):
        pass


# 详情
class DetailView(View):
    def get(self, request, sku_id):
        try:
            # 接收
            sku_id = int(sku_id)
            goods_sku = GoodsSKU.objects.get(pk=sku_id)
            context = {
                'goods_sku': goods_sku
            }
            return render(request, 'sup_goods/detail.html', context)
        except:
            return redirect(reverse('sup:个人中心'))

    def post(self, request):
        pass



