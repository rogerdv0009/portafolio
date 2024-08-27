from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import Testimony
# Create your views here.

# Listado de los testimonios existentes
class TestimonyListView(ListView):
    model = Testimony
    template_name = "testimonies/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(state=True)
        search = self.request.GET.get("search_input")
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(job__icontains=search),
                state = True
            ).distinct()
        return queryset



# Detalle del testimonio
class TestimonyDetailView(DetailView):
    model = Testimony
    template_name = "testimonies/detail.html"

