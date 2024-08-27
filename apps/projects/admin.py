from django.contrib import admin
from .models import Project
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ProjectResource (resources.ModelResource):
    class Meta:
        model = Project

@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title','description']
    list_display = ('title','created_date','state')
    resource_class = ProjectResource