from django.urls import path
from .views import ExperienceListView, ExperienceDetailView

urlpatterns = [
    path("list/", ExperienceListView.as_view(), name="Experiences_List"),
    path("detail/", ExperienceDetailView.as_view(), name="Experiences_Detail"),
]
