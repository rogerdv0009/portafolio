from django.urls import path
from .views import TechnologyListView, TechnologyDetailView

urlpatterns = [
    path("list/", TechnologyListView.as_view(), name="Technologies_List"),
    path("detail/", TechnologyDetailView.as_view(), name="Technologies_Detail"),
]
