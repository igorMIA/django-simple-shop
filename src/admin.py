from django.contrib import admin
from .models import Category, Goods, Carousel, OrderModel


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')

admin.site.register(Category)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Carousel)
admin.site.register(OrderModel)
