from unicodedata import name
from django.urls import include,path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'), 
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('category/<str:slug>/', get_post, name='post'),
]