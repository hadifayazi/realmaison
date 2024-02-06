from .models import Enquiry
from .serializers import EnquiriesSerializer
from realmaisonAPI.settings.development import DEFAULT_FROM_EMAIL
from django.core.mail import send_mail
from rest_framework import generics, permissions, status
from rest_framework.response import Response


class EnquiriesView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EnquiriesSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            subject = data['subject']
            name = data['name']
            email = data['email']
            message = data['message']
            recipient_list = [DEFAULT_FROM_EMAIL]

            send_mail(subject, name, email, message, recipient_list, fail_silently=True,)
            enquiry = Enquiry(name, email, message, subject)
            enquiry.save()
            return Response({'success': 'Your enquiry has been recorded'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
