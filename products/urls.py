from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<product_id>', views.show_product, name='show_product'),
]
