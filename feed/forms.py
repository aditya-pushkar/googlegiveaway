from django import forms
from .models import UplodedPic

import re

# txt = "The rain in Spain"
# x = re.search("fuc k", txt)

# if x != None:
#     print("no error")
# else:
#     print(" error" )


class UplodeImageForm(forms.ModelForm):
    
    class Meta:
        model = UplodedPic
        fields = (
            'insta',
            'fb',
            'img',

        )
    
    def clean_fb(self):
        fb = self.cleaned_data['fb']
        src = re.search("facebook.com", fb)

        if src == None:
            raise forms.ValidationError(" THIS IS NOT FACEBOOK LINK PLEASE PROVIDE CORRECT LINK ")
        return fb
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['insta'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': ' Your instagram username (optional)'})
        self.fields['fb'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Your facebook profile link (optional) '})
      