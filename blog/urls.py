from unicodedata import name
from django.urls import include,path

from .views import *


urlpatterns = [
    path('', index, name='home'), 
    path('category/<str:slug>/', get_category, name='category'),
]