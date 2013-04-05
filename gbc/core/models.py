from django.db import models
from django_resized import ResizedImageField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Slide(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(max_length=512)
    image = ResizedImageField(max_width=1170, max_height=500, upload_to='slides', help_text='Dimensions: 1180x500px')
    
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.title

class Tile(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(max_length=512)
    image = ResizedImageField(max_width=360, max_height=150, upload_to='tiles', help_text='Dimensions: 360x150px')

    def __unicode__(self):
        return self.title