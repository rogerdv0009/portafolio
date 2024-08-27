from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import Experience
# Create your views here.

# Listado de las experiencias existentes
class ExperienceListView(ListView):
    model = Experience
    template_name = "experiences/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(state=True)
        search = self.request.GET.get("search_input")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(city__icontains=search),
                state = True
            ).distinct()
        return queryset



# Detalle de la experiencia
class ExperienceDetailView(DetailView):
    model = Experience
    template_name = "experiences/detail.html"

