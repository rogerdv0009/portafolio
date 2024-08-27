from django.urls import path
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path("list/", ProjectListView.as_view(), name="Projects_List"),
    path("detail/", ProjectDetailView.as_view(), name="Projects_Detail"),
]
