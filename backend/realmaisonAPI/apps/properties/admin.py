from django.contrib import admin
from .models import Property
from .models import ListingImage


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city',  'price',
                    'bedrooms', 'bathrooms', 'house_type', 'surface', 'sale_type')
    list_filter = ('country', 'city', 'sale_type', 'price')

    # def is_published(self, obj):
    #     return obj.get('is_published')

    # is_published.boolean = True
    # is_published.short_description = 'Is Published'


admin.site.register(Property, PropertyAdmin)
admin.site.register(ListingImage)
