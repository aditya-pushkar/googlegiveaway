from django.urls import path
from . import views
app_name  = 'feed'

urlpatterns = [
    path('social/', views.feed, name='feed')
]
