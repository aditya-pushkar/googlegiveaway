from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView


# Model Import
from .models import Category, Product

# Create your views here.

class Home(ListView):
    context_object_name = 'item'
    template_name = 'store/home.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['is_lastchance'] = Product.objects.filter(is_lastchance=True)
        context['is_trending'] = Product.objects.filter(is_trending=True)
        return context


def category_list(request, category_slug=None):
    # Category.objects.filter(slug=category_slug)
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context =  {
        'category': category,
        'products': products
    }
    return render(request, 'store/category.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'store/product_detail.html', context)


class Product_all(ListView):
    context_object_name = 'product'
    model = Product
    template_name = 'store/products_all.html'