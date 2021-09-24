from django.forms import ModelForm
from .models import Billboard

class UplodeImageForm(ModelForm):
    
    class Meta:
        model = Billboard
        fields = (
            'image',

        )