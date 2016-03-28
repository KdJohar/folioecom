# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 15:35
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('meta_description', models.CharField(blank=True, max_length=500, verbose_name='Meta Description')),
                ('meta_keywords', models.CharField(blank=True, max_length=250, verbose_name='Meta Keywords')),
                ('body', ckeditor.fields.RichTextField()),
                ('publish', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='blogs',
            name='category',
            field=models.ManyToManyField(to='blogs.Categories'),
        ),
    ]