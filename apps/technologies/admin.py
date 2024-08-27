from django.contrib import admin
from .models import Technology
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class TechnologyResource (resources.ModelResource):
    class Meta:
        model = Technology

@admin.register(Technology)
class TechnologyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title','created_date','state')
    resource_class = TechnologyResource