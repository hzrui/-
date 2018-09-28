from django.contrib import admin

from sup_goods.models import Category, Unit, GoodsSPU, Gallery, GoodsSKU, Banner, Activity, ActivityZone, \
    ActivityZoneGoods

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


# 首页表注册Banner的模型到后台
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


# 注册Activity的模型到后台
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass


# 注册ActivityZone的模型到后台

class ActivityZoneAdminInline(admin.StackedInline):
    model = ActivityZoneGoods
    extra = 2


# 首页活动专区商品列表
# @admin.register(ActivityZone)
# class ActivityZoneGoodsAdmin(admin.ModelAdmin):
#     inlines = [
#         ActivityZoneAdminInline
#     ]


class ActivityZoneGoodsInline(admin.TabularInline):
    model = ActivityZoneGoods
    extra = 3
    fields = ['activity_zone','goods_sku']

@admin.register(ActivityZone)
class ActivityZoneAdmin(admin.ModelAdmin):
    inlines = [
        ActivityZoneGoodsInline
    ]

