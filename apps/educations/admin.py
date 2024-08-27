from django.contrib import admin
from .models import Education
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class EducationResource (resources.ModelResource):
    class Meta:
        model = Education

@admin.register(Education)
class EducationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title','subtitle']
    list_display = ('title','created_date','state')
    resource_class = EducationResource

