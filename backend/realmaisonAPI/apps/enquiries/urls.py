from django.urls import path
from . import views

urlpatterns = [
    path('', views.EnquiriesView.as_view, name="send-enquiry"),
]
