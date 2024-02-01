from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from apps.ratings.serializers import RatingSerializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    last_name = serializers.CharField(source='user.last_name')
    firs_name = serializers.CharField(source='user.first_name')
    email = serializers.EmailField(source='user.email')
    full_name = serializers.SerializerMethodField(read_only=True)
    country = CountryField(name_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    def get_reviews(self, obj):
        reviews = obj.agent_review.all()
        serializer = RatingSerializer(reviews, many=True)
        return serializer.data


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
