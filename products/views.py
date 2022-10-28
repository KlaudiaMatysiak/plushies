from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from .models import Product, Category


def shop(request):
    """ A view to show all the products in the shop"""

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                print("error, search empty")
                return redirect(reverse('shop'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(color__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/shop.html', context)


def show_product(request, product_id):
    """ A view to show a product in details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/show_product.html', context)
