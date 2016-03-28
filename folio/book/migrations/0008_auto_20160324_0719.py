# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_seometadata_seo_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='slug',
            field=models.SlugField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]