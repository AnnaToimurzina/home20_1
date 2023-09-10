from django.contrib import admin

from catalog.models import Category, Product, Version

'''admin.site.register(Category)
admin.site.register(Product)'''

@admin.register(Category)
class CategoryAdmin (admin.ModelAdmin):
    list_display = ('id', 'category')
    search_fields = ('category',)

@admin.register(Product)
class ProductAdmin (admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('name', 'price', 'category')
    search_fields = ('name', 'description')

@admin.register(Version)
class VersionAdmin (admin.ModelAdmin):
    list_display = ('id', 'product', 'version_name', 'version_number', 'is_active',)
    search_fields = ('product', 'version_name', 'version_number',)
    list_filter = ('product', 'version_name', 'version_number', 'is_active',)


