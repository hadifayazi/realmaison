from django.urls import path
from . import views

urlpatterns = [

    path("<int:profile_id>", views.create_agent_review, name="agent-review"),
]
