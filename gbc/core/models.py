from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Slide(models.Model):
    title_sv = models.CharField(max_length=256)
    title_en = models.CharField(max_length=256, blank=True, null=True)
    content_sv = models.TextField(max_length=512)
    content_en = models.TextField(max_length=512, blank=True, null=True)
    image = models.ImageField(upload_to='slides', help_text='Dimensions: 1280x500px')
    link = models.CharField(max_length=256, help_text='ie. "http://gbc.se/events" or just "/event/1"', blank=True,null=True )
    link_text_sv = models.CharField(max_length=64, help_text='Text for the button/link', blank=True,null=True)
    link_text_en = models.CharField(max_length=64, help_text='Text for the button/link', blank=True,null=True)

    def __unicode__(self):
        return self.title_sv

class Tile(models.Model):
    IMAGE_FORMAT = ( ('R','Rectangular'), ('C', 'Circular') )

    title_sv = models.CharField(max_length=256)
    title_en = models.CharField(max_length=256, blank=True, null=True)
    content_sv = models.TextField(max_length=512)
    content_en = models.TextField(max_length=512, blank=True, null=True)
    image = models.ImageField(upload_to='tiles', help_text='Dimensions: 360x150px rectangular.')
    link = models.CharField(max_length=256, help_text='ie. "http://gbc.se/event/1" or just "/event/1"', blank=True,null=True)
    link_file = models.ImageField(upload_to='files', help_text='Upload a file that will be accessed by the link. Overrides normal link.', blank=True, null=True)
    link_text_sv = models.CharField(max_length=64, help_text='Text for the button/link', blank=True, null=True)
    link_text_en = models.CharField(max_length=64, help_text='Text for the button/link', blank=True, null=True)
    image_format = models.CharField(max_length=2, choices=IMAGE_FORMAT, default='C')

    def __unicode__(self):
        return self.title_sv


class Featurette(models.Model):
    title_sv = models.CharField(max_length=256)
    title_en = models.CharField(max_length=256, blank=True, null=True)
    subtitle_sv = models.CharField(max_length=256)
    subtitle_en = models.CharField(max_length=256, blank=True, null=True)
    content_sv = models.TextField(max_length=512)
    content_en = models.TextField(max_length=512, blank=True, null=True)
    image = models.ImageField(upload_to='featurettes', help_text='Dimensions: 512x512px')
    link = models.CharField(max_length=256, help_text='ie. "http://gbc.se/event/1" or just "/event/1"', blank=True, null=True)

    def __unicode__(self):
        return self.title_sv + ' ' + self.subtitle_sv

class Menu_item(models.Model):
    label = models.CharField(max_length=128)
    mouseover = models.CharField(max_length=256, help_text="Tooltip")
    link = models.CharField(max_length=256, help_text='ie. "http://gbc.se/events" or just "/events"')    

    def __unicode__(self):
        return self.label

class Sponsor(models.Model):
    title_sv = models.CharField(max_length=128, help_text="Sponsor name")
    title_en = models.CharField(max_length=128, help_text="Sponsor name", blank=True, null=True)
    description_sv = models.CharField(max_length=512, help_text="Optional description", blank=True, null=True)
    description_en = models.CharField(max_length=512, help_text="Optional description", blank=True, null=True)
    image = models.ImageField(upload_to='sponsor', help_text='')
    link = models.CharField(max_length=256, help_text='ie. "http://www.5d.se" ', blank=True, null=True)

    def __unicode__(self):
        return self.title_sv