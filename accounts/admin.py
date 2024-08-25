from django.contrib import admin
from django.urls import path
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import (
    CustomUserCreationForm, CustomUserChangeForm
)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'age', 'is_staff']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)