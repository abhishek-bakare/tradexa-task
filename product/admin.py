from django.contrib import admin
from .models import Products

# here i register product model for appearing in django admin

admin.site.register(Products)