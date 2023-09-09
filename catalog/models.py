from django.db import models

from catalog.templatetags.my_tags import mediapath

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField()

    def str(self):
        return self.id, self.category

    class Meta:
        verbose_name = 'Категория товара'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', verbose_name='foto', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    active_version = models.BooleanField(default=True, verbose_name='product_active_version')

    def str(self):
        return self.id_product, self.name, self.category, self.price

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Product',)
    version_name = models.CharField(max_length=100, verbose_name='Название версии', )
    version_number = models.CharField(max_length=10, verbose_name='Номер версии', )
    is_active = models.BooleanField(default=True, verbose_name='Is Active', )

    def __str__(self):
        return f'{self.product} - Version {self.version_number}'

    class Meta:
        verbose_name = 'Version'
        verbose_name_plural = 'Versions'
        ordering = ('product', 'version_name', 'version_number', 'is_active',)
