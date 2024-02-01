from django.contrib import admin
from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city',  'price',
                    'bedrooms', 'bathrooms', 'house_type', 'surface', 'sale_type')
    list_filter = ('country', 'city', 'sale_type', 'is_published', 'price')


admin.site.register(Property, PropertyAdmin)
