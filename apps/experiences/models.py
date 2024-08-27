from django.db import models

from apps.base.models import BaseModel
from apps.technologies.models import Technology
# Create your models here.

class Action(BaseModel):
    '''Model definition for Action.'''

    title = models.CharField("Title", max_length=150, null=False, blank=False)

    class Meta:
        '''Meta definition for Action.'''

        verbose_name = 'Action'
        verbose_name_plural = 'Actions'

    def __str__(self):
        return self.title

#********************************************************************************************

class Experience(BaseModel):
    '''Model definition for Experience.'''

    title = models.CharField("Title", max_length=150, null=False, blank=False)
    city = models.CharField("City", max_length=150)
    technologies = models.ManyToManyField(Technology)
    actions = models.ManyToManyField(Action)

    class Meta:
        '''Meta definition for Experience.'''

        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.title