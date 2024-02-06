from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllPropertiesList.as_view(), name='all-properties-list'),
    path('realtor', views.RealtorPropertiesList.as_view(), name="all-realtor-properties"),
    path('create', views.PropertyCreate.as_view(), name='create-property'),
    path('update/<slug:slug>', views.PropertyUpdate.as_view(), name="update-property"),
    path('details/<slug:slug>', views.PropertyViewsDetail.as_view(), name="property-details"),
    path('delete/<slug:slug>', views.DeleteProperty.as_view(), name="delete-property"),
    path('photos/upload/<slug:slug>', views.PropertyPhotosUploadView.as_view(), name="upload-photos"),
    path('search', views.PropertySearchView.as_view(), name="search-properties"),
]
