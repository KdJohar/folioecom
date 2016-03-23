from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
from django.utils.text import slugify

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

def image_upload_to(instance, filename):
    title = slugify(instance.title)
    file_extention = filename.split(".")[1]
    file_name = "%s.%s"%(title, file_extention)
    return "book/%s/%s"%(title, file_name)

class Books(models.Model):

    LANGUAGE_CHOICE = (
        ('en', 'english'),
    )

    BINDING_CHOICE = (
        ('pb', 'paperback'),
    )

    title = models.CharField(max_length=500, unique=True)
    slug = models.CharField(max_length=500, unique=True)
    image = models.ImageField(upload_to=image_upload_to)
    category = models.ForeignKey(SubCategory)
    isbn10 = models.CharField(validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10')], max_length=10)
    isbn13 = models.CharField(validators=[RegexValidator(regex='^.{13}$', message='Length has to be 13')], max_length=13)
    publisher = models.ForeignKey(Publisher)
    author = models.ManyToManyField(Author)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICE)
    binding = models.CharField(max_length=2, choices=BINDING_CHOICE)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def get_image(self):
        return self.image.url


    def save(self, *args, **kwargs):
        cost = int(self.cost_price)
        percent_margin = 15
        paking_cost = 5
        cost = cost + (cost*percent_margin)/100
        self.selling_price = cost+paking_cost
        super(Books, self).save(*args, **kwargs)



    def __unicode__(self):
        return self.title