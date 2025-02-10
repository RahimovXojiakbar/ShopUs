from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .models import Product
from .forms import CommentForm

def index_view(request):
    return render(request, 'home.html')

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