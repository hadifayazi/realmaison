import logging
import django_filters

from .models import Property
from .pagination import PropertyPagination
from .serializers import PropertySerializer

from rest_framework import filters, generics, permissions, status
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
