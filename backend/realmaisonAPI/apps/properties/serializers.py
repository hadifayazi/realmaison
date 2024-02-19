from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import Property, PropertyViews, ListingImage


class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ('id', 'image', 'property')

    # def create(self, validated_data):
    #     """
    #     Override the create method to associate the image with the property.
    #     """
    #     property_instance = validated_data.get('property')
    #     image = validated_data.get('image')
    #     listing_image = ListingImage.objects.create(property=property_instance, image=image)
    #     return listing_image


class PropertySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    country = CountryField(name_only=True)
    images = ListingImageSerializer(source='image', many=True, )

    class Meta:
        model = Property
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.username

    def __str__(self):
        return f"Image {self.id}"


class PropertyViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyViews
        fields = '__all__'
