from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import Property, PropertyViews


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
