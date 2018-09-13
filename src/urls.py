from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('categories/', views.categories, name='categories'),
	path('categories/<category>/', views.cat, name='category'),
	path('product/<title>/', views.product, name='product'),
	path('cart/', views.cart, name='cart'),
	path('cart/add/', views.cart_add, name='cart_add'),
	path('cart/clear/', views.cart_clear, name='cart_clear'),
	path('order/', views.order, name='order'),
	path('order/make/', views.order_make, name='order_make'),
	path('i18n/', include('django.conf.urls.i18n')),
	path('search/', views.MySearchView.as_view(), name='search_view'),
]

# for static in dev mod
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
