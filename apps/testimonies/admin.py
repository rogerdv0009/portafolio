from django.contrib import admin
from .models import Testimony
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class TestimonyResource (resources.ModelResource):
    class Meta:
        model = Testimony

@admin.register(Testimony)
class TestimonyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name','job']
    list_display = ('name','created_date','state')
    resource_class = TestimonyResource