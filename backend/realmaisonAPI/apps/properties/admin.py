from django.contrib import admin
from .models import Property, ListingImage, PropertyViews


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city',  'price',
                    'bedrooms', 'bathrooms', 'house_type', 'surface', 'sale_type')
    list_filter = ('country', 'city', 'sale_type', 'price')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'images':
            kwargs['queryset'] = ListingImage.objects.none()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    # def is_published(self, obj):
    #     return obj.get('is_published')

    # is_published.boolean = True
    # is_published.short_description = 'Is Published'


admin.site.register(Property, PropertyAdmin)
admin.site.register(ListingImage)
admin.site.register(PropertyViews)
