from django.contrib import admin

from catalog.models import Category, Product


'''admin.site.register(Category)
admin.site.register(Product)'''

@admin.register(Category)
class CategoryAdmin (admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('category',)

@admin.register(Product)
class ProductAdmin (admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('name', 'price', 'category')
    search_fields = ('name', 'description')


