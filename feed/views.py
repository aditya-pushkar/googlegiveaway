from django.views.generic.list import ListView
from django.shortcuts import render
from .models import UplodedPic

from django.core.paginator import Paginator


# Create your views here.

# def feed(request, page=1):
#     qs = UplodedPic.objects.all()
#     paginator  = Paginator(qs, 1) # 12 user per page

#     #we dont't need to handle the case where the page parameter
#     #is not an integer beacause our url oly accept integers 

#     try:
#         qs = paginator.page(page)

#     except Exception as EmptyPage:

#         #if we exceed the page limit we return the last page 
#         qs = paginator.page(paginator.num_pages)


#     context = {
#         'qs': qs
#     }
    
#     return render(request, 'feed/feed.html', context)

class Feed(ListView):
    model = UplodedPic
    template_name  = 'feed/feed.html'
    context_object_name = 'qs'
    paginate_by = 1

    queryset = UplodedPic.objects.all()