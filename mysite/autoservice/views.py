from django.shortcuts import render, get_object_or_404

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


def authors(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'cars.html', context=context)


def author(request, car_id):
    single_car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car.html', {'car': single_car})