from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .models import Product
from .forms import CommentForm
from django.core.paginator import Paginator
from .forms import SearchForm


def index_view(request):
    return render(request, 'home.html')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def comment_view(request,uuid):
    product = get_object_or_404(Product, uuid=uuid)
    comments = product.comments.all()
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('comment', uuid=product.uuid)

    return render(request, 'comment.html', {
        'product': product,
        'comments': comments,
        'form': form,
    })

def detail_view(request):
    return render(request, 'product-detail.html')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def new_products(request):
    queryset = models.Product.objects.all().order_by('-created')
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products':page_obj
    }
    return render(request, 'new_products.html', context)

    
def search_view(request):
    form = SearchForm(request.GET)
    queryset = form.cleaned_data['queryset'] if form.is_valid() else ''
    
    product_result = models.Product.objects.filter(name__icontains=queryset)
    
    
    context = {
        'form': form,
        'products': product_result,
        
    }
    return render(request, 'home.html', context)