import folium
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.educations.models import Education
from apps.services.models import Service
from apps.experiences.models import Experience
from apps.projects.models import Project
from apps.technologies.models import Technology
from apps.testimonies.models import Testimony

# Create your views here.

class MainView(TemplateView):
    template_name = "index.html"

    initialMap = folium.Map(location=[20.3725728,-76.6803028], zoom_start=9)
    coordinates = (20.386083, -76.64801)
    folium.Marker(coordinates).add_to(initialMap)

    def getServices(self):
        cont = Service.objects.filter(state=True).count()
        services = None
        if cont:
            if cont > 0 and cont < 4:
                services = Service.objects.filter(state=True)
            else:
                services = Service.objects.filter(state=True)[:3]
        return services


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = self.getServices()
        context["projects"] = Project.objects.filter(state=True)
        context["educations"] = Education.objects.filter(state = True)
        context["experiences"] = Experience.objects.filter(state = True)
        context["technologies"] = Technology.objects.filter(state = True)
        context["map"] = self.initialMap._repr_html_()
        return context
