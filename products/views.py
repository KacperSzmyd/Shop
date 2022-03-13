from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    all_categories = Category.objects.all()
    return render(request, 'index.html', {'categories' : all_categories})

def category(request, id):
    all_categories = Category.objects.all()
    category_user = Category.objects.get(pk=id)
    products_by_category = Products.objects.filter(category=category_user)
    return render(request, 'products_by_category.html', {'categories': all_categories,
                                          'category' : category_user,
                                          'products' : products_by_category})

def product(request, id):
    all_categories = Category.objects.all()
    product_user_or_404 = get_object_or_404(Products, pk=id)
    return render(request, 'product.html', {'product' : product_user_or_404,
                                            'categories': all_categories})