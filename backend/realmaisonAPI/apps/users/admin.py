from django.contrib import admin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email',
                    'is_staff', 'is_superuser', 'is_active', 'date_join')
    list_display_links = ('id', 'email')
    list_filter = ('email', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    readonly_fields = ('date_join',)
    list_editable = ('is_staff', 'is_superuser', 'is_active')
    exclude = ('password', 'password2')  # Exclude password from list view

    fieldsets = (
        (_('Credentials'), {'fields': ('username', 'email', 'password')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        (_('Groups'), {'fields': ('groups',)}),  # Correct attribute name
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'is_staff', 'password', 'password2', 'is_active', 'date_join')}),
    )

    date_hierarchy = 'date_join'
    ordering = ('email', 'username')


admin.site.register(CustomUser, CustomUserAdmin)
