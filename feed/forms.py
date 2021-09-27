from django.forms import ModelForm
from .models import UplodedPic

class UplodeImageForm(ModelForm):
    
    class Meta:
        model = UplodedPic
        fields = (
            'img',

        )