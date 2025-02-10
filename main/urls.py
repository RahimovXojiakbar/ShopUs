from . import views
from django.urls import path    
from .views import product_detail

urlpatterns = [
   path('', views.index_view),
   path('product/<str:uuid>/', product_detail, name='product_detail')
]

