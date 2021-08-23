from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib import admin


# Create your models here.
admin.site.site_title = 'Jamii'
admin.site.site_header = 'Jamii Admin Panel'


class Blog(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, default='Jamii')
    date_posted = models.DateTimeField(default=timezone.now)
    content = RichTextField()
    cover = models.ImageField(upload_to='images/', default='default.jpg')

    def __str__(self):
        return self.title
