from refferal.models import Refferal
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView


# Model Import
from .models import Category, Product
from order.models import Order
from feed.models import UplodedPic

# Create your views here.


def home(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        # get the code of the person who reffered
        refferal = Refferal.objects.get(code=code)
        request.session['ref_profile'] = refferal.id
        print('id', refferal.id)
    except:
        pass
    print(request.session.get_expiry_age())

    is_lastchance =  Product.objects.filter(is_lastchance=True)
    is_trending = Product.objects.filter(is_trending=True)
    
    context = {
        'is_lastchance': is_lastchance,
        'is_trending': is_trending
    }

    return render(request, 'store/home.html', context)


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

    # user profile recommendation 
    pr = product.id 
    ord = Order.objects.filter(product__id=pr)
    
    
    # user_name = []
    # user_img = []
    user_dict = {}
    for item in ord:
        up = UplodedPic.objects.filter(user=item.user.id)
        
        for item in up:
            # user_name.append(item.user.user_name)
            # user_img.append(item.img.url)
            # um = (item.user.user_name)
            # ui = (item.img.url)    
            user_dict.update({f"{item.user.user_name}": f"{item.img.url}"})
    
    print(user_dict)
 
   
    context = {
        'product': product,
        'user_dict': user_dict       
    }
   
    return render(request, 'store/product_detail.html', context)


class Product_all(ListView):
    context_object_name = 'product'
    model = Product
    template_name = 'store/products_all.html'