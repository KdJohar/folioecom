from __future__ import unicode_literals

from django.db import models
# Create your models here.

class NewsLetter(models.Model):
    email = models.EmailField(unique=True)
    def __unicode__(self):
        return self.email


