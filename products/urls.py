from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:product_id>/', views.show_product, name='show_product'),
    path('add/', views.add_product, name='add_product'),
]
