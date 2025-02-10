from django.shortcuts import render
from . import models

def index_view(request):
    return render(request, 'home.html')

def detail_view(request):
    return render(request, 'product-detail.html')