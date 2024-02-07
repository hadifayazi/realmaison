import logging
import django_filters

from .models import Property, PropertyViews
from .pagination import PropertyPagination
from .serializers import PropertySerializer, PropertyViewsSerializer, ListingImageSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
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
        slug = self.kwargs.get('slug')
        property = get_object_or_404(Property, slug=slug)
        if property.user != self.request.user:
            raise PermissionDenied("You do not have permission to update this property.")
        return Property.objects.filter(slug=slug)

    def update(self, request, *args, **kwargs):
        property = self.get_object()
        updated_data = request.data.get('property', {})
        serializer = PropertySerializer(property, data=updated_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PropertySerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        property_data = request.data.get('property', {})
        serializer = PropertySerializer(data=property_data)
        if serializer.is_valid():
            serializer.save(user=user)
            logger.info(
                f"User {user.username}, created property: ${serializer.data['title']}, reference: {serializer.data.get('reference')}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProperty(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'slug'

    def get_queryset(self):
        return Property.objects.all()

    def destroy(self, request, *args, **kwargs):
        property = self.get_object()
        if property.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this property.")

        property.delete()

        return Response({"message": "Property deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class PropertyPhotosUploadView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ListingImageSerializer

    def create(self, request, *args, **kwargs):
        property_slug = kwargs.get('slug')
        property_instance = Property.objects.get(slug=property_slug)

        if property_instance.user != request.user:
            return Response({"detail": "You do not have permission to upload photos for this property."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = ListingImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(property=property_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertySearchView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PropertySerializer

    def post(self, request, *args, **kwargs):
        queryset = Property.objects.filter(is_published=True)
        data = request.data

        house_type = data['house_type'].lower()
        queryset = queryset.filter(house_type__iexact=house_type)

        sale_type = data['sale_type'].lower()
        queryset = queryset.filter(sale_type__iexact=sale_type)

        price = data['price']
        price = data['bedrooms']
        if price == '0+':
            price = 0
        elif price == '$50000+':
            price = 50000
        elif price == '$150000+':
            price = 150000
        elif price == '$250000+':
            price = 250000
        elif price == '350000+':
            price = 4
        elif price == '350000+':
            price = 5
        elif price == '450000+':
            price = 450000
        queryset = queryset.filter(price__gte=price)

        bedrooms = data['bedrooms']
        if bedrooms == '0+':
            bedrooms = 0
        elif bedrooms == '1+':
            bedrooms = 1
        elif bedrooms == '2+':
            bedrooms = 2
        elif bedrooms == '3+':
            bedrooms = 3
        elif bedrooms == '4+':
            bedrooms = 4
        elif bedrooms == '5+':
            bedrooms = 5
        elif bedrooms == '6+':
            bedrooms = 6
        queryset = queryset.filter(bedrooms__gte=bedrooms)

        serializer = PropertySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
