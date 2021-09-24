from django.db import models
from django.conf import settings

# Create your models here.

class Billboard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True)
    image = models.ImageField(blank=True)
   
    # total pic uploded by user  
    # def total_pic_uploded(self):
    #     qs = Billboard.objects.all()

    #     pic = 0
    #     for item in qs:
    #         if item.user == self.user:
    #             pic += 1
    #     return pic

