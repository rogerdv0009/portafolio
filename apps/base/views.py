from django.shortcuts import render
from django.views.generic import TemplateView

from apps.educations.models import Education
from apps.experiences.models import Experience
from apps.projects.models import Project
from apps.technologies.models import Technology
from apps.testimonies.models import Testimony

# Create your views here.

class MainView(TemplateView):
    template_name = "index.html"
