from django.urls import path
from .views import EducationListView, EducationDetailView

urlpatterns = [
    path("list/", EducationListView.as_view(), name="Educations_List"),
    path("detail/", EducationDetailView.as_view(), name="Educations_Detail"),
]
