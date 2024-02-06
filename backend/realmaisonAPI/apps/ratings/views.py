from apps.profiles.models import Profile
from .models import Rating
from .serializers import RatingSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

User = get_user_model()


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_agent_review(request, profile_id):
    user = request.user
    profile = get_object_or_404(Profile, id=profile_id)
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user, profile=profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
