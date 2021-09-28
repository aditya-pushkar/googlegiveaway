from django.db import models
from django.conf import settings



# Create your models here.


class UplodedPic(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # get user's insta user_name
    insta = models.CharField(max_length=20, null=True, blank=True)
    # user facebook profile link
    fb = models.URLField(max_length=100, blank=True)

    img = models.ImageField(blank=False)


    class Meta:
        ordering = ("-id", )
   

    def __str__(self):
        return f"{self.user.user_name}"