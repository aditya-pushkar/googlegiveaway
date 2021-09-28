from django.views.generic.list import ListView
from django.shortcuts import render
from .models import UplodedPic




class Feed(ListView):
    model = UplodedPic
    template_name  = 'feed/feed.html'
    context_object_name = 'qs'
    paginate_by = 2

    queryset = UplodedPic.objects.all()