from . import views
from django.urls import path    
from .import views

urlpatterns = [
   path('', views.index_view, name='home'),
   path('comment/<str:uuid>/', views.comment_view, name='comment'),
   path('detail/', views.detail_view, name='product-detail'),
   path('news/', views.new_products, name='new_products'),
   path('search/', views.search_view, name='search'),

]

