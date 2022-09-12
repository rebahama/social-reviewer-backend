""" register the model to the admin site"""
from django.contrib import admin
from .models import Comments

admin.site.register(Comments)
