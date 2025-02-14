from . import views
from django.urls import path    
from .import views

urlpatterns = [
   path('', views.index_view, name='home'),
   path('comment/<str:uuid>/', views.comment_view, name='comment'),
   path('detail/', views.detail_view, name='product-detail'),
   path('news/', views.new_products, name='new_products'),
   path('search/', views.search_view, name='search'),
   path('shop/', views.shop_view, name='shop'),
   path('wishlist/', views.wishlist_view, name='wishlist'),
   path('cart/', views.cart_view, name='cart'),
   path('profile/', views.profile_view , name='profile'),
   path('contact/', views.contact_view, name='contact'),
   path('privacy/', views.privacy, name='privacy'),
   path('terms/', views.terms_view, name='terms'),
   path('login/', views.login_view, name='login'),



]

