from django.urls import path
from . import views

urlpatterns = [
    path("me", views.GetProfile.as_view(), name="my_profile"),
    path("update/<uid>", views.UpdateProfile.as_view(), name="update_profile"),
    path("agents", views.AgentProfileList.as_view(), name="agents"),
]
