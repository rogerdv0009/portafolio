from django.db import models

from apps.base.models import BaseModel
# Create your models here.

class Service(BaseModel):
    '''Model definition for Service.'''

    title = models.CharField("Title", max_length=150, null=False, blank=False)
    description = models.TextField("Description", null=False, blank=False)
    icon = models.CharField("Icon", max_length=50, null=True, blank=True, default="fas fa-code")

    class Meta:
        '''Meta definition for Service.'''

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title