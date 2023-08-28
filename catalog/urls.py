from django.urls import path, include

from catalog.apps import CatalogConfig
from catalog.views import index, about, contact

app_name=CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    ]