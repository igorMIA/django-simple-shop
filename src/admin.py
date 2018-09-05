from django.contrib import admin
from .models import Category, Goods, Carousel, OrderModel


class GoodsAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'is_published')
	actions = ['make_published', 'un_published']

	def make_published(self, request, queryset):
		status = queryset.update(is_published=True)
		if status == 1:
			self.message_user(request, '1 product was successfully marked as published')
		else:
			self.message_user(request, '{} products were successfully marked as published'.format(status))
	make_published.short_description = 'Mark selected products as published'

	def un_published(self, request, queryset):
		status = queryset.update(is_published=False)
		if status == 1:
			self.message_user(request, '1 product was successfully marked as un published')
		else:
			self.message_user(request, '{} products were successfully marked as un published'.format(status))
	un_published.short_description = 'Mark selected products as un published'

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'is_published')
	actions = ['make_published', 'un_published']

	def make_published(self, request, queryset):
		status = queryset.update(is_published=True)
		if status == 1:
			self.message_user(request, '1 category was successfully marked as published')
		else:
			self.message_user(request, '{} products were successfully marked as published'.format(status))
	make_published.short_description = 'Mark selected products as published'

	def un_published(self, request, queryset):
		status = queryset.update(is_published=False)
		if status == 1:
			self.message_user(request, '1 category was successfully marked as un published')
		else:
			self.message_user(request, '{} categories were successfully marked as un published'.format(status))
	un_published.short_description = 'Mark selected categories as un published'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Carousel)
admin.site.register(OrderModel)
