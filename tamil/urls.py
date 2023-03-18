from django.urls import path
from tamil.views import *
app_name='tamil'
urlpatterns=[
    path('hotc/',hotc,name='hotc'),
]