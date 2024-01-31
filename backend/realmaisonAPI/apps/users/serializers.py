from rest_framework import serializers
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserSerializer(serializers.ModelSerializer):
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
