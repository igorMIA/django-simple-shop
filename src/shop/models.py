from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=20)
    is_published = models.BooleanField(verbose_name=_('is_published'), default=True)
    image = models.FileField(verbose_name=_('image'), upload_to='image/cat/')

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.title


class Goods(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=20)
    is_published = models.BooleanField(verbose_name=_('is_published'), default=True)
    is_recommend = models.BooleanField(verbose_name=_('is_recommend'), default=False)
    is_top = models.BooleanField(verbose_name=_('is_top'), default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_('category'))
    price = models.FloatField(verbose_name=_('price'))
    image = models.FileField(verbose_name=_('image'), upload_to='image/goods/')
    text = models.TextField(verbose_name=_('text'))

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ('category', 'title')

    def __str__(self):
        return self.title


class Carousel(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=100)
    text = models.CharField(verbose_name=_('text'), max_length=200)
    image = models.FileField(verbose_name=_('image'), upload_to='image/carousel/')

    class Meta:
        verbose_name = _('slide')
        verbose_name_plural = _('slides')

    def __str__(self):
        return self.title


class OrderModel(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)
    surname = models.CharField(verbose_name=_('surname'), max_length=100)
    email = models.EmailField(verbose_name=_('email'))
    tel = models.CharField(verbose_name=_('tel'), max_length=100)
    products = models.TextField(verbose_name=_('products'))

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def __str__(self):
        return '{} №{}'.format(_('order'), self.id)
