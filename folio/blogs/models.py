from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse('category_view', kwargs={'slug': self.slug})


    def __unicode__(self):
        return self.name




class Blogs(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Title')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    meta_description = models.CharField(max_length=500, verbose_name='Meta Description', blank=True)
    meta_keywords = models.CharField(max_length=250, verbose_name='Meta Keywords', blank=True)
    body = RichTextField()
    category = models.ManyToManyField(Categories)
    publish = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Blogs"


    def get_absolute_url(self):
        return reverse('blog_view', kwargs={'slug': self.slug})


    def __unicode__(self):
        return self.title
