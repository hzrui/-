from django.contrib import admin

from sup_goods.models import Category, Unit, GoodsSPU, Gallery, GoodsSKU

admin.site.site_header = '超级电商管理平台'
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 商品分类
    pass


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    # 商品单位
    pass


@admin.register(GoodsSPU)
class GoodsSPUAdmin(admin.ModelAdmin):
    # 商品SPU
    pass


# 关联相册
class GoodsSKUAdminInLine(admin.TabularInline):
    model = Gallery
    extra = 3
    fields = ['goods_sku', 'img_url']


# 注册GoodsSKU的模型到后台
@admin.register(GoodsSKU)
# 定制显示效果
class GoodsSKUAdmin(admin.ModelAdmin):
    # 商品SPU
    # 关联模型展示
    inlines = [
        GoodsSKUAdminInLine
    ]
