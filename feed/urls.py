from django.urls import path
from .views import Feed

app_name  = 'feed'

urlpatterns = [
    path('social/', Feed.as_view(), name='feed')
]
