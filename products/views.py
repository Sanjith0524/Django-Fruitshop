from django.shortcuts import render
from django.http import HttpResponse
from.models import Product
def index(requests):
    products = Product.objects.all()
    return render(requests,'index.html',{'products':products})

def new(requests):
    return HttpResponse('New products')