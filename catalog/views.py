from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index(request):
    return render(request, "catalog/index.html")


'''def about(request):
    return render(request, "catalog/about.html")'''

def about(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'

    }

    return render(request, 'catalog/about.html', context)

def contact(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')
    context = {'title': 'Контакты'}

    return render(requests, 'catalog/contact.html', context)



