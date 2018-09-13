from haystack import indexes
from .models import Goods


class GoodsIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')
	desc = indexes.CharField(model_attr='text')

	def get_model(self):
		return Goods

	def index_queryset(self, using=None):
		return self.get_model().objects.all()
