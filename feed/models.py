from django.db import models
from django.conf import settings
from PIL import Image

# Create your models here.


class UplodedPic(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.ImageField(blank=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.img.path)

        if image.height > 350 or image.width>350:
            output_size = (350, 350)
            image.thumbnail(output_size)
            image.save(self.img.path)


   

    def __str__(self):
        return f"{self.user.user_name}"