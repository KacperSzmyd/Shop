from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    all_categories = Category.objects.all()
    return render(request, 'index.html', {'all_categories' : all_categories})

def category(request, id):
    category_user = Category.objects.get(pk=id)
    return HttpResponse(category_user)

def product(request, id):
    product_user = Products.objects.get(pk=id)
    return HttpResponse(product_user)