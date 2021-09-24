from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:ref_code>/', views.home, name='main-view'),
    path('giveaway/<slug:category_slug>/', views.category_list, name='category_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('view/all/', views.Product_all.as_view(), name='product_all'),

]
