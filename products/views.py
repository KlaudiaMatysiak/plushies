from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category


def shop(request):
    """ A view to show all the products in the shop"""

    products = Product.objects.distinct('name').order_by(
        'products_product.name', 'price')
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/shop.html', context)


def show_product(request, product_id):
    """ A view to show a product in details"""

    product = get_object_or_404(Product, pk=product_id)
    products = Product.objects.filter(name=product.name)

    context = {
        'product': product,
        'products': products,
    }

    return render(request, 'products/show_product.html', context)
