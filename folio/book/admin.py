from django.contrib import admin
from .models import Author, Publisher, Category, SubCategory, Books, Inventory, SeoMetaData
# Register your models here.


class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'category', 'isbn10', 'isbn13', 'cost_price', 'selling_price')
    list_filter = ('category', 'author', 'publisher')
    search_fields = ('title', )
    prepopulated_fields = {"slug": ("title",)}

class SubCategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'category', )
    list_filter = ('category', )
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("name",)}


class InventoryAdmin(admin.ModelAdmin):

    list_display = ('book', 'quantity')
    search_fields = ('book__title', )

class SeoMetaDataAdmin(admin.ModelAdmin):

    list_display = ('book', 'seo_done', )
    search_fields = ('book__title', )

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Books, BookAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(SeoMetaData, SeoMetaDataAdmin)