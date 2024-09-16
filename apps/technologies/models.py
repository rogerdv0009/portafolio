from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from apps.base.models import BaseModel
# Create your models here.

def validateImageSize(value):
    filesize = value.size
    if filesize > 1 * 1024 * 1024:  # 1MB
        raise ValidationError("El tamaño máximo permitido es 1MB")

class Technology(BaseModel):
    '''Model definition for Technology.'''

    title = models.CharField("Title", max_length=150, null=False, blank=False, unique=True)
    image = models.ImageField("Image", upload_to="technologies/", max_length=None, null=True, blank=True, validators=[FileExtensionValidator(['jpg','jpeg','png','gif','webp']),validateImageSize])
    stars = models.PositiveSmallIntegerField(default=0, null=False, blank=False)

    class Meta:
        '''Meta definition for Technology.'''

        verbose_name = 'Technology'
        verbose_name_plural = 'Technologys'

    def __str__(self):
        return self.title

    def ListOfStars(self):
        if self.stars > 0:
            stars_list = []
            star_class = "fas fa-star"
            for i in range(self.stars):
                stars_list.append(star_class)
            return stars_list
        else:
            return None