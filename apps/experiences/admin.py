from django.contrib import admin
from .models import Action, Experience
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ActionResource (resources.ModelResource):
    class Meta:
        model = Action

@admin.register(Action)
class ActionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title','created_date','state')
    resource_class = ActionResource

class ExperienceResource (resources.ModelResource):
    class Meta:
        model = Experience

@admin.register(Experience)
class ExperienceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title','city']
    list_display = ('title','created_date','state')
    resource_class = ExperienceResource