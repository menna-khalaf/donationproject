from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('mobile_phone', 'profile_picture', 'birthdate', 'facebook_profile', 'country')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('mobile_phone', 'profile_picture', 'birthdate', 'facebook_profile', 'country')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'mobile_phone', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'mobile_phone')
