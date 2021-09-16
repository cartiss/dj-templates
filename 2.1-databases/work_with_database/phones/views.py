from django.shortcuts import render, redirect
from phones.models import Phone
import csv

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = Phone.objects.values()

    if sort == 'name':
        phones = Phone.objects.order_by('name').values()

    elif sort == 'min_price':
        phones = Phone.objects.order_by('price').values()

    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price').values()

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).values()
    print(phone)
    context = {'phone': phone[0]}
    return render(request, template, context)



