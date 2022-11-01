from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ A view of the cart contents """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    A view of adding a quantity of the selected product
    to the shopping cart
    """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request,
            f'Added {quantity} x {product.name} \
                size {product.size} to your cart')
    else:
        cart[item_id] = quantity
        messages.success(
            request,
            f'Added {quantity} x {product.name} \
                size {product.size} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def modify_cart(request, item_id):
    """
    A view of modifying a quantity of the selected product
    to the specified amount
    """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ A view of removing product from cart """

    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
