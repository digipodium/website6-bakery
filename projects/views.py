from django.shortcuts import render
from .models import Product

# Create your views here.

def homeview(request):
    
    cat = request.GET.get('cat')
    if cat:
        products = Product.objects.filter(category=cat)
    else:
        products = Product.objects.all()
    context = {"products" : products}
    return render(request,'index.html',context)


