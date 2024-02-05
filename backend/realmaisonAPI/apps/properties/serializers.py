from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import Property, PropertyViews, ListingImage


class PropertySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.username


class PropertyViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyViews
        fields = '__all__'


class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ('id', 'image', 'property')

    def create(self, validated_data):
        """
        Override the create method to associate the image with the property.
        """
        property_instance = validated_data.get('property')
        image = validated_data.get('image')
        listing_image = ListingImage.objects.create(property=property_instance, image=image)
        return listing_image
