from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Products


admin.site.register(Products)
