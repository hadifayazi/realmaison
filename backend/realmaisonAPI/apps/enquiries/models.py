from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Enquiry(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    phone_number = PhoneNumberField(verbose_name=_("Phone number"), max_length=30)
    email = models.EmailField(verbose_name=_("Email"))
    subject = models.CharField(_("Subject"), max_length=100)
    message = models.TextField(verbose_name=_("Message"))

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = _("Enquiry")
        verbose_name_plural = _("Enquiries")
