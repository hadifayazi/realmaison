from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer, UpdateProfileSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class AgentProfileList(generics.ListAPIView):
    queryset = Profile.objects.filter(is_agent=True)
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class GetProfile(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = self.request.user
        profile = get_object_or_404(Profile, user=user)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProfile(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateProfileSerializer

    def patch(self, request, *args, **kwargs):
        profile_id = self.kwargs.get('uid')
        profile = get_object_or_404(Profile, id=profile_id)

        data = request.data
        serializer = UpdateProfileSerializer(data=data, instance=profile, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
