from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/about.html'


def contact(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')
    context = {'title': 'Контакты'}

    return render(requests, 'catalog/contact.html', context)

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:about')

class ProductUpdateView(UpdateView):
    pass



