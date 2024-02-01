from collections.abc import Iterable
import random
import string
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


User = get_user_model()


class PropertyPublishManager(models.Model):
    def get_queryset(self):
        return super(PropertyPublishManager, self).get_queryset().filter(is_published=True)


class ListingImage(models.Model):
    """Listing images."""
    property = models.ForeignKey(
        'Property', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property-photos/%Y/%m/%d')


class Property(models.Model):
    class HouseType(models.TextChoices):
        MAISON = 'Maison', _("Maison")
        APPARTEMENT = 'Apartment', _("Apartment")
        VILLA = 'Villa', _("Villa")
        OFFICE = 'Office', _("Office")
        COMMERCE = 'Commerce', _("Commerce")
        OTHER = 'Other', _("Other")

    class SaleType(models.TextChoices):
        FOR_SALE = 'For sale', _("For sale")
        FOR_RENT = 'For rent', _("For rent")

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="agent_client",
                             verbose_name=_("Agent, Seller, Client"))
    title = models.CharField(max_length=150,  verbose_name=_("Title"))
    slug = AutoSlugField(populate_from="title", max_length=200, unique=True, always_update=True)
    referece = models.CharField(verbose_name=_("Referece"), max_length=200, blank=True, unique=True)
    description = models.TextField(verbose_name=_("Description"), blank=True)
    country = CountryField(verbose_name=_("Country"), default="FR", blank_label=_("Select Country"))
    address = models.CharField(verbose_name=_("Address"), max_length=200)
    city = models.CharField(verbose_name=_("City"), max_length=100)
    state = models.CharField(verbose_name=_('State'), max_length=100)
    zipcode = models.CharField(verbose_name=_("zipcode"), max_length=20)
    sale_type = models.CharField(
        max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE, verbose_name=_("Sale Type"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    bedrooms = models.IntegerField(verbose_name=_("Bedrooms"))
    bathrooms = models.IntegerField(verbose_name=_("Bathrooms"))
    house_type = models.CharField(
        max_length=50, choices=HouseType.choices, default=HouseType.APPARTEMENT, verbose_name=_("House Type"))
    surface = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Surface"))
    image = models.ManyToManyField(
        ListingImage, blank=True, related_name='properties', verbose_name=_("Images"))
    is_published = models.BooleanField(default=True, verbose_name=_("Published status"))
    views = models.IntegerField(default=0, verbose_name=_("Views"))
    list_date = models.DateTimeField(default=timezone.now, blank=True)

    objects = models.Manager()
    is_published = PropertyPublishManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')

    def generate_reference(self):
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self.generate_reference()
        super().save(*args, **kwargs)
