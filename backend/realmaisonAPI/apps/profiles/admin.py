from django.contrib import admin
from .models import Profile


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ("id", "user", 'gender', 'phone_number', 'country', 'city')
    list_filter = ('gender', 'city')
    list_display_links = ('id', 'user')


admin.site.register(Profile, ProfilesAdmin)
