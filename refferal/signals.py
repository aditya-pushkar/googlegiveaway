from .models import Refferal
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_created_profile(sender, instance, created, *args, **kwargs):
    if created:
        Refferal.objects.create(user=instance)
