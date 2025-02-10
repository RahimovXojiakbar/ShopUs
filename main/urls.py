from . import views
from django.urls import path    
from .views import product_detail

urlpatterns = [
<<<<<<< HEAD
   path('', views.index_view),
   path('product/<str:uuid>/', product_detail, name='product_detail')
=======
   path('', views.index_view, name='home'),
   path('product-detail', views.detail_view, name='product-detil')
>>>>>>> b67f6800eb91572785243a1f4cfed23695df9496
]

