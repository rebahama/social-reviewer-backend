"""Adding the category model to the admin site in Django/admin"""
from django.contrib import admin
from .models import Category

admin.site.register(Category)
