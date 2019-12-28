from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('contacts', contacts, name='contacts'),
    path('send_comment', send_comment, name='send_comment'),
]
