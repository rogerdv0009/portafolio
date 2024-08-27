from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import Project
# Create your views here.

# Listado de los proyectos existentes
class ProjectListView(ListView):
    model = Project
    template_name = "projects/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(state=True)
        search = self.request.GET.get("search_input")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search),
                state = True
            ).distinct()
        return queryset



# Detalle del proyecto
class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/detail.html"

