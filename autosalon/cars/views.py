from django.shortcuts import render
from .models import Brand, Car

def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    return render(request, 'home.html', {'brands': brands, 'cars': cars})

def brand_detail(request, id):
    brand = Brand.objects.get(id=id)
    cars = Car.objects.filter(brand=brand)
    return render(request, 'brand_detail.html', {'brand': brand, 'cars': cars})

def car_detail(request, id):
    car = Car.objects.get(id=id)
    return render(request, 'car_detail.html', {'car': car})

