from django.contrib import admin
from .models import product, categories

# Register your models here.
admin.site.register(product)
admin.site.register(categories)