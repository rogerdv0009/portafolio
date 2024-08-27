from django.db import models

from apps.base.models import BaseModel
# Create your models here.

class Education(BaseModel):
    '''Model definition for Education.'''

    title = models.CharField("Title", max_length=150, null=False, blank=False)
    subtitle = models.CharField("Subtitle", max_length=150, null=False, blank=False)
    start_date = models.DateField("Start Date", auto_now=False, auto_now_add=False)
    end_date = models.DateField("End Date", auto_now=False, auto_now_add=False)

    class Meta:
        '''Meta definition for Education.'''

        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        return self.title
