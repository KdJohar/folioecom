from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from .models import Categories, Blogs
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
    fields = (('name',), ('slug',), )


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': CKEditorWidget } , }
    list_display = ['title', 'date', 'time', 'publish']
    fields = (('title', 'publish',), ('slug',),  ('category',),('meta_description','meta_keywords',), 'body')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('category', 'publish')
    search_fields = ['title']


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Blogs, BlogAdmin)