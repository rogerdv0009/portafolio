from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from apps.base.models import BaseModel
from apps.technologies.models import Technology
# Create your models here.

def validateImageSize(value):
    filesize = value.size
    if filesize > 2 * 1024 * 1024:  # 1MB
        raise ValidationError("El tamaño máximo permitido es 1MB")


class Project(BaseModel):
    '''Model definition for Project.'''

    title = models.CharField("Title", max_length=150, null=False, blank=False)
    image = models.ImageField("Image", upload_to="project/", max_length=None, null=True, blank=True, validators=[FileExtensionValidator(['jpg','jpeg','png','gif','webp']),validateImageSize])
    description = models.TextField("Description", null=False, blank=False)
    technologies = models.ManyToManyField(Technology)
    frontend = models.URLField("Frontend", max_length=200, null=True, blank=True)
    backend = models.URLField("Backend", max_length=200, null=True, blank=True)

    class Meta:
        '''Meta definition for Project.'''

        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def getTechnologies(self):
        technologies = [technology for technology in self.technologies.all().values_list('title', flat=True)]
        return technologies