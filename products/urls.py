from django.urls import path
from .views import *

urlpatterns = [
    path('', products_all, name='products'),
    path('best/', products_best, name='products_best'),
    path('filter/<cat>/', cat_set, name='cat_set'),
    path('<prd>/', prd_det, name='prd_det'),
    path('<prd>/rate/<rt>/', rate_prd, name='rate_prd'),
]
