from django.shortcuts import render
from django.http import HttpResponse
from .models import Product ,Clint ,Market
# Create your views here.
def Product(request):
    return render(request,'products/products.html',{"product_card" : Product.objects.all(),'clints_card':Clint.objects.all(),'markets_card':Market.objects.all()})
    
