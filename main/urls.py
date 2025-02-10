from . import views
from django.urls import path    

urlpatterns = [
   path('', views.index_view, name='home'),
   path('product-detail', views.detail_view, name='product-detil')
]

