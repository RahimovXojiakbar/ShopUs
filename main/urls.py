from . import views
from django.urls import path    
from .import views

urlpatterns = [
   path('', views.index_view),
   path('comment/<str:uuid>/', views.comment_view, name='comment'),
   path('detail/', views.detail_view, name='product-detail')
]

