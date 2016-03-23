from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name
