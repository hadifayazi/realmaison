from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllPropertiesList.as_view(), name='all_properties_list'),
]
