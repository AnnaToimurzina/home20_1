from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


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
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:about')

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""

        context_data = super().get_context_data(**kwargs)

        version_form_set = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = version_form_set(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = version_form_set(instance=self.object)

        return context_data

    def form_valid(self, form):
        """Called if all forms are valid.
         Creates a Version instance along with the main Product instance."""

        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        if formset.is_valid():
            formset.instance = self.object # Привязываем версию к продукту
            formset.save()

        return super().form_valid(form)



