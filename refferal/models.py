from django.db import models
from django.conf import settings
from refferal.utils import generate_ref_code

# Create your models here.

class Refferal(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.user_name}---{self.code}"


    def get_recommended_profiles(self):
        qs = Refferal.objects.all()

        reff = []
        for profile in qs:
            if profile.recommended_by == self.user:
                reff.append(profile)
        total_reff  = len(reff)*199
        return total_reff
        

    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_ref_code()
            self.code = code
            pass
        super().save(*args, **kwargs)