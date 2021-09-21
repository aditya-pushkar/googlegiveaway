from django.db import models
from store.models import Product
from django.conf import settings



# it store all user order that had been successfuly purchased
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.user_name}--{self.product.title}"


class Payment(models.Model):
    order_id = models.CharField(max_length=50, null=False)
    payment_id = models.CharField(max_length=50)
    
    # user_product only store the item which had been purchased by user
    user_product = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # all the product store that thagt had been purchased or the transection of item had been failed
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)