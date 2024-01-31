from rest_framework import serializers
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="profile.gender")
    phone_number = serializers.CharField(source="profile.phone_number")
    prifile_photo = serializers.ImageField(source="profile.prifile_photo")
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField(source="get_full_name")
    country = serializers.CharField(source="profile.country")
    city = serializers.CharField(source="profile.city")

    class Meta:
        model: CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'gender',
                  'phone_number', 'prifile_photo',  'country', 'city', 'full_name')

    def get_fist_name(self, obj: CustomUser):
        return obj.first_name

    def get_last_name(self, obj: CustomUser):
        return obj.last_name

    def to_representation(self, instance):
        representation = super(UserSerializer).to_representation(instance)
        if instance.is_superuser:
            representation['Admin'] = True
        return representation


class CustomCreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'is_staff', 'is_superuser', 'is_active', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}, 'password2': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': _('Passwords do not match.')})
        return data

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            is_staff=validated_data['is_staff'],
            is_superuser=validated_data['is_superuser'],
            is_active=validated_data['is_active'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
