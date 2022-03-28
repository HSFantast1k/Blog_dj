from django.urls import include,path

from .views import *


urlpatterns = [
    path('', index, name='home'), 
    path('__debug__/', include('debug_toolbar.urls')),
]