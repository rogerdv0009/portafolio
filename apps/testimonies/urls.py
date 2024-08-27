from django.urls import path
from .views import TestimonyListView, TestimonyDetailView

urlpatterns = [
    path("list/", TestimonyListView.as_view(), name="Testimonies_List"),
    path("detail/", TestimonyDetailView.as_view(), name="Testimonies_Detail"),
]
