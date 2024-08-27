from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from apps.base.models import BaseModel
# Create your models here.

def validateImageSize(value):
    filesize = value.size
    if filesize > 1 * 1024 * 1024:  # 1MB
        raise ValidationError("El tamaño máximo permitido es 1MB")


class Testimony(BaseModel):
    '''Model definition for Testimony.'''

    name = models.CharField("Name", max_length=150, null=False, blank=False)
    job = models.CharField("Job", max_length=150)
    description = models.TextField("Description", null=False, blank=False)
    image = models.ImageField("Image", upload_to="testimonies/", max_length=None, null=True, blank=True, validators=[FileExtensionValidator(['jpg','jpeg','png','gif','webp']),validateImageSize])
    facebook = models.URLField("Facebook", max_length=200, null=True, blank=True)
    linkedin = models.URLField("Linked In", max_length=200, null=True, blank=True)
    instagram = models.URLField("Instagram", max_length=200, null=True, blank=True)
    twitter = models.URLField("Twitter", max_length=200, null=True, blank=True)

    class Meta:
        '''Meta definition for Testimony.'''

        verbose_name = 'Testimony'
        verbose_name_plural = 'Testimonies'

    def __str__(self):
        return self.name