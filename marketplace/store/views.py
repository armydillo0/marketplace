from django.shortcuts import render
from django.http import HttpResponse
from profile.models import Product


def index(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request,'store/index.html',context)



# Create your views here.
