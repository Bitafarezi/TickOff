from django.shortcuts import render, redirect
# from django.views.generic import ListView

# from .models import Category, Book

# Create your views here.


def homeView(request):
    return render(request, 'base.html')