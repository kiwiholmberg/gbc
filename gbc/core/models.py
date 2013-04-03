from django.db import models

class Slide(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=256)
    image = models.ImageField(upload_to='slides')

    def __unicode__(self):
        return self.title