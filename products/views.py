from django.shortcuts import render
from .models import Product


def shop(request):
    """ A view to show all the products in the shop"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/shop.html', context)


