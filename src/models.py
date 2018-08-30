from django.db import models


class Category(models.Model):
	title = models.CharField(max_length=20)
	image = models.FileField(upload_to='image/cat/')
	
	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.title


class Goods(models.Model):
	title = models.CharField(max_length=20)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	price = models.FloatField()
	image = models.FileField(upload_to='image/goods/')
	text = models.TextField()

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
		ordering = ('category', 'title')

	def __str__(self):
		return self.title


class Carousel(models.Model):
	title = models.CharField(max_length=100)
	text = models.CharField(max_length=200)
	image = models.FileField(upload_to='image/carousel/')

	class Meta:
		verbose_name = 'Слайд'
		verbose_name_plural = 'Слайды'

	def __str__(self):
		return self.title


class OrderModel(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	email = models.EmailField()
	tel = models.CharField(max_length=100)
	products = models.TextField()

	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

	def __str__(self):
		return 'Заказ №{}'.format(self.id)
