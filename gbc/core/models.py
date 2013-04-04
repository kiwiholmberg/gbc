from django.db import models
from django_resized import ResizedImageField

class Slide(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=256)
    image = ResizedImageField(max_width=1170, max_height=500, upload_to='slides')

    def __unicode__(self):
        return self.title