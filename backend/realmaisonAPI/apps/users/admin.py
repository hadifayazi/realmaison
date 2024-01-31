from django.contrib import admin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    ordering = ('email', 'username')
    list_display = ('id', 'email', 'username', 'first_name', 'last_name',
                    'is_staff', 'is_superuser', 'is_active', 'date_joined', 'last_login')
    list_display_links = ('id', 'email')
    list_filter = ('email', 'is_staff', 'is_superuser', 'is_active', )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    readonly_fields = ('date_joined',)
    list_editable = ('is_staff', 'is_superuser', 'is_active')

    fieldsets = (
        (_('Credentials'), {'fields': ('email', 'password')}),
        (_('User Details'), {'fields': ('username', 'first_name', 'last_name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'is_staff', 'is_superuser', 'is_active', 'date_joined'),
        }),
    )

    date_hierarchy = 'date_joined'


admin.site.register(CustomUser, CustomUserAdmin)
