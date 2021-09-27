from django.shortcuts import render
from .models import UplodedPic


# Create your views here.

def feed(request):
    qs = UplodedPic.objects.all()

    context = {
        'qs': qs
    }
    
    return render(request, 'feed/feed.html', context)
