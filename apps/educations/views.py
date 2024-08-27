from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import Education
# Create your views here.

# Listado de las educaciones existentes
class EducationListView(ListView):
    model = Education
    template_name = "educations/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(state=True)
        search = self.request.GET.get("search_input")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(subtitle__icontains=search),
                state = True
            ).distinct()
        return queryset



# Detalle de la educacion
class EducationDetailView(DetailView):
    model = Education
    template_name = "educations/detail.html"


