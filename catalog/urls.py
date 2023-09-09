from django.urls import path

from blog.views import BlogCreateView, BlogUpdateView
from catalog.apps import CatalogConfig
from catalog.views import contact, ProductListView, ProductUpdateView, ProductCreateView

app_name=CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='about'),
    path('contact/', contact, name='contact'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    ]