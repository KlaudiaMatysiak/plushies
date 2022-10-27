from django.shortcuts import render, get_object_or_404
from .models import Product


def shop(request):
    """ A view to show all the products in the shop"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/shop.html', context)


def show_product(request, product_id):
    """ A view to show a product in details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/show_product.html', context)
