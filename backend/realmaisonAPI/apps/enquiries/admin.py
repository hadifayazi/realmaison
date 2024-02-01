from django.contrib import admin
from .models import Enquiry


class EnquiriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'phone_number', 'email', 'subject', 'message')


admin.site.register(Enquiry, EnquiriesAdmin)
