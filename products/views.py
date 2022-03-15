from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
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

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Nieprawidłowy login lub hasło')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def register(request):
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            user = register_form.cleaned_data.get('username')
            messages.success(request, 'Utworzono konto dla ' + user)

            return redirect('login')


    context = {'form' : register_form}
    return render(request, 'register.html', context)