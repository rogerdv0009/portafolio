from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import Technology
# Create your views here.

# Listado de las tecnologias existentes
class TechnologyListView(ListView):
    model = Technology
    template_name = "technologies/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(state=True)
        search = self.request.GET.get("search_input")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search),
                state = True
            ).distinct()
        return queryset



# Detalle de la tecnologia
class TechnologyDetailView(DetailView):
    model = Technology
    template_name = "technologies/detail.html"

