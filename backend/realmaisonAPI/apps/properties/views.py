import logging
import django_filters

from .models import Property, PropertyViews
from .pagination import PropertyPagination
from .serializers import PropertySerializer, PropertyViewsSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


logger = logging.getLogger(__name__)


class PropertyFilter(django_filters.FilterSet):
    house_type = django_filters.CharFilter(
        field_name="house_type", lookup_expr='iexact')

    sale_type = django_filters.CharFilter(
        field_name="sale_type", lookup_expr='iexact')

    price = django_filters.NumberFilter()
    price__gte = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price__lte = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    city = django_filters.CharFilter(field_name="city", lookup_expr="iexact")
    country = django_filters.CharFilter(field_name="country", lookup_expr="iexact")

    class Meta:
        model = Property
        fields = ['house_type', 'sale_type', 'price', 'city', 'country']


class AllPropertiesList(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    pagination_class = PropertyPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = PropertyFilter
    search_fields = ('reference', 'country', 'city')
    ordering_fields = ('list_date')


class RealtorPropertiesList(generics.ListAPIView):
    serializer_class = PropertySerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = PropertyPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = PropertyFilter
    search_fields = ('reference', 'country', 'city')
    ordering_fields = ('list_date')

    def get_queryset(self):
        return Property.objects.filter(user=self.request.user).order_by('-list_date')


class PropertyViewsAPIView(generics.ListAPIView):
    serializer_class = PropertyViewsSerializer
    queryset = PropertyViews.objects.all()


class PropertyViewsDetail(APIView):
    def get(self, request, slug):
        property = Property.objects.get(slug=slug)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
            logger.info(ip)
        else:
            ip = self.request.META.get('REMOTE_ADDR')

        if not PropertyViews.objects.filter(property=property, ip=ip).exists():
            PropertyViews.objects.create(property=property, ip=ip)
            property.views += 1
            property.save()

        serializer = PropertySerializer(property, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PropertyUpdate(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PropertySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        property = get_object_or_404(Property, slug=self.kwargs.get('slug'))
        if property.user != self.request.user:
            raise PermissionDenied("You do not have permission to update this property.")
        return property

    def update(self, request, *args, **kwargs):
        property = self.get_object()
        serializer = PropertySerializer(property, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PropertySerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            logger.info(
                f"User {user.username}, created property: ${serializer.data['title']}, reference: {serializer.data.get('reference')}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
