from django.shortcuts import render

# Create your views here.

from django.urls import path
from .models import Car, Service, Order

def index(request):
    paslaugu_kiekis = Service.objects.count()
    atliktu_uzsakymu_kiekis = Order.objects.filter(status__exact='a').count()
    automobiliu_kiekis = Car.objects.count()

    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'paslaugu_kiekis': paslaugu_kiekis,
        'atliktu_uzsakymu_kiekis': atliktu_uzsakymu_kiekis,
        'automobiliu_kiekis': automobiliu_kiekis,
    }

    # renderiname base.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)