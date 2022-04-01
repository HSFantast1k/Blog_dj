from unicodedata import name
from django.urls import include,path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'), 
    path('category/<str:slug>/', get_category, name='category'),
    path('category/<str:slug>/', get_post, name='post'),
]