from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField

User = get_user_model()


class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = "Male", _("Male")
        Female = "Female", _("Female")
        Other = "Other", _("Other")

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, verbose_name=_('Gender'), choices=Gender.choices, default="")
    phone_number = PhoneNumberField(region='FR',)
    country = CountryField(verbose_name=_('Country'), blank=True, default='FR')
    city = models.CharField(max_length=100, verbose_name=_('City'), blank=True, null=True)
    about_me = models.TextField(verbose_name=_("About me"), default="", blank=True, null=True)
    prifile_photo = models.ImageField(verbose_name=_("Profile photo"),
                                      upload_to="profile_photos", blank=True, null=True)
    is_buyer = models.BooleanField(default=False, verbose_name=_("Buyer"))
    is_seller = models.BooleanField(default=False, verbose_name=_("Seller"))
    is_agent = models.BooleanField(default=False, verbose_name=_("Agent"))
    rating = models.DecimalField(verbose_name=_("Rating"), decimal_places=2, max_digits=5, null=True)
    nb_reviews = models.PositiveIntegerField(default=0, verbose_name=_("Number of reviews"), null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
