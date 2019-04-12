from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Category, Goods, Carousel, OrderModel
from .forms import AddCart, Order
from haystack.generic_views import SearchView
from django.core.mail import send_mail
from django.utils.translation import gettext as _


def index(request):
    context = {}
    context['slides'] = Carousel.objects.all()
    context['categories'] = Category.objects.filter(is_published=True)
    paginator = Paginator(Category.objects.filter(is_published=True), 9)
    context['recommend'] = Goods.objects.filter(is_recommend=True)
    context['top'] = Goods.objects.filter(is_top=True)
    context['site_title'] = _('main')
    return render(request, 'shop/index.html', context)


def categories(request):
    context = {}
    paginator = Paginator(Category.objects.filter(is_published=True), 9)
    page = request.GET.get('page')
    context['categories'] = paginator.get_page(page)
    if 'last_product' in request.session:
        context['last_product'] = Goods.objects.get(title=request.session['last_product'])
    context['site_title'] = _('categories')
    return render(request, 'shop/categories.html', context)


def cat(request, category):
    context = {}
    paginator = Paginator(Goods.objects.filter(category=category, is_published=True), 9)
    page = request.GET.get('page')
    context['products'] = paginator.get_page(page)
    context['categories'] = Category.objects.filter(is_published=True)
    if 'last_product' in request.session:
        context['last_product'] = Goods.objects.get(title=request.session['last_product'])
    context['site_title'] = Category.objects.get(id=category).title
    return render(request, 'shop/category.html', context)


def product(request, title):
    request.session['last_product'] = title
    context = {}
    product = Goods.objects.get(title=title)
    context['categories'] = Category.objects.filter(is_published=True)
    if 'last_product' in request.session:
        context['last_product'] = Goods.objects.get(title=request.session['last_product'])
    context['product'] = product
    context['site_title'] = title
    return render(request, 'shop/product.html', context)


def cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = dict()
        request.session['cart']['product_id'] = list()
        request.session['cart']['count'] = list()
    context = {}
    context['categories'] = Category.objects.filter(is_published=True)
    if 'last_product' in request.session:
        context['last_product'] = Goods.objects.get(title=request.session['last_product'])
    products = []
    counts = request.session['cart']['count']
    for product_id in request.session['cart']['product_id']:
        products.append(Goods.objects.get(id=product_id))
    sum = 0
    for product, count in zip(products, counts):
        sum += product.price * count
    context['sum'] = sum
    context['products'] = zip(products, counts)
    context['site_title'] = _('cart')
    return render(request, 'shop/cart.html', context)


def cart_add(request):
    if 'cart' not in request.session:
        request.session['cart'] = dict()
        request.session['cart']['product_id'] = list()
        request.session['cart']['count'] = list()
    if request.method == 'POST':
        form = AddCart(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            count = form.cleaned_data['count']
            request.session['cart']['product_id'].append(int(product_id))
            request.session['cart']['count'].append(int(count))
            request.session.modified = True
    return redirect('/cart/')


def cart_clear(request):
    request.session['cart']['product_id'] = []
    request.session['cart']['count'] = []
    request.session.modified = True
    return redirect('/cart/')


def order(request):
    context = {}
    context['categories'] = Category.objects.filter(is_published=True)
    if 'last_product' in request.session:
        context['last_product'] = Goods.objects.get(title=request.session['last_product'])
    context['site_title'] = _('make_order')
    return render(request, 'shop/order.html', context)


def order_make(request):
    context = {}
    context['categories'] = Category.objects.filter(is_published=True)
    if 'last_product' in request.session:
        context['last_product'] = Goods.objects.get(title=request.session['last_product'])
    if request.method == 'POST':
        form = Order(request.POST)
        if form.is_valid():
            context['site_title'] = _('success_order')
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            tel = form.cleaned_data['tel']
            out = '{}:\n'.format(_('order'))
            for product_id, count in zip(request.session['cart']['product_id'], request.session['cart']['count']):
                product = Goods.objects.get(id=product_id)
                out += '{}: {} грн {}: {}\n'.format(_('product'), product.title, _('count'), count)
            OrderModel.objects.create(name=name, surname=surname, email=email, tel=tel, products=out)
            send_mail(
                _('new_order'),
                '{}:\n{}: {}\n{}: {}\n{}: {}\n{}: {}\n'.format(_('client'), _('name'), name, _('surname'), surname,
                                                               _('tel'), tel, _('email'), email) + out,
                'service@shop.com',
                ['admin@shop.com'],
                fail_silently=False,
            )
        else:
            context['site_title'] = _('error_order')
    return render(request, 'shop/order_status.html', context)


class MySearchView(SearchView):

    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.filter(is_published=True)
        if 'last_product' in self.request.session:
            context['last_product'] = Goods.objects.get(title=self.request.session['last_product'])
        context['site_title'] = '{} | {}'.format(_('search'), self.queryset.query)
        return context
