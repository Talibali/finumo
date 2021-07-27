from project.apps.user import models
from django.contrib import admin


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    list_display = (
        'id', 'user_type', 'first_name', 'last_name', 'profile_photo', 'email', 'email_verified', 'country_code', 'mobile',
        'mobile_verified', 'gender', 'dob', 'status','is_active', 'is_staff', 'created_at')
    list_display_links = ('id',)
    search_fields = ('id', 'first_name', 'last_name', 'email', 'mobile')
    list_per_page = 20

admin.site.register(models.Profile, ProfileAdmin)    