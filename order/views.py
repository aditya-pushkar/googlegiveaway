from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from time import time
import razorpay

# internal import
from store.models import Product 
from .models import Order, Payment

# razorpay client 
client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))

@login_required
def checkout(request, slug):
    product = Product.objects.get(slug=slug)

    user = request.user

    action = request.GET.get('action')
    order = None
    payment = None
    error = None
    if action == "create_payment":

        try:
            user_product = Order.objects.get(user=user, product=product)
            error = "You are already enroled in this cource"
        except:
            pass
        # checking the error 
        if error is None:

            amount = int((product.price)*100)
            currency = "INR"
            notes = {
                "email": user.email,
                "name": user.user_name

            }
            
            receipt = f"GoogleGiveaway-{int(time())}"
            order = client.order.create({
                'receipt':receipt,
                'notes':notes,
                'amount':amount,
                'currency':currency
            })
            

            payment = Payment.objects.create(
                user=user,
                product=product,
                order_id=order.get('id'),    
            )
            payment.save()

    context = {
        'product': product,
        'order': order,
        'payment': payment,
        'error':error 
    }
    return render(request, 'order/checkout.html', context)

@csrf_exempt
def verifyPayment(request):
    if request.method == 'POST':
        data = request.POST
        try:
            client.utility.verify_payment_signature(data)
            # data.get method does not throw exception but data['data'] thow's the exception
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']

            print(razorpay_payment_id, razorpay_order_id)
            
            # .get gives us one query data and . fliter gives us more then 1 query data
            payment = Payment.objects.get(order_id=razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True

            order = Order.objects.create(user=payment.user, product=payment.product)
            order.save()
            print("UserProduct", order.id)

            payment.user_product = order
            payment.save()
            return render(request, template_name='order/my_order.html')

        except Exception as ex:
            return HttpResponse("Invalid payment Detail")
    
    
    
