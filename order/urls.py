from django.urls import path
from . import views 

app_name  = 'order'

urlpatterns = [
    path('<str:slug>/', views.checkout, name='checkout'),
    path('payment/verifyPayment/', views.verifyPayment, name='verify_payment'),
]
