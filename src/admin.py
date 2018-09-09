from django.contrib import admin
from .models import Category, Goods, Carousel, OrderModel
from django.utils.translation import gettext_lazy as _


class GoodsAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'is_published', 'is_recommend')
	actions = ['make_published', 'un_published']

	def make_published(self, request, queryset):
		status = queryset.update(is_published=True)
		if status == 1:
			self.message_user(request, _('one_product_success'))
		else:
			self.message_user(request, '{} {}'.format(status, _('few_products_success')))
	make_published.short_description = _('mark_products_published')

	def un_published(self, request, queryset):
		status = queryset.update(is_published=False)
		if status == 1:
			self.message_user(request, _('un_one_product_success'))
		else:
			self.message_user(request, '{} {}'.format(status, _('un_few_products_success')))
	un_published.short_description = _('un_mark_products_published')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'is_published')
	actions = ['make_published', 'un_published']

	def make_published(self, request, queryset):
		status = queryset.update(is_published=True)
		if status == 1:
			self.message_user(request, _('one_category_success'))
		else:
			self.message_user(request, '{} {}'.format(status, _('few_categories_success')))
	make_published.short_description = _('mark_categories_published')

	def un_published(self, request, queryset):
		status = queryset.update(is_published=False)
		if status == 1:
			self.message_user(request, _('un_one_category_success'))
		else:
			self.message_user(request, '{} {}'.format(status, _('un_few_categories_success')))
	un_published.short_description = _('un_mark_categories_published')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Carousel)
admin.site.register(OrderModel)
