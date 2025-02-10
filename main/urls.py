from . import views
from django.urls import path    

urlpatterns = [
   # path('', views.index_view),
   path('', views.my_view ,name='lang')
]

