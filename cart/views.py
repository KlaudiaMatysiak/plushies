from django.shortcuts import render, redirect


def view_cart(request):
    """ A view of the cart contents """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    A view of adding a quantity of the selected product
    to the shopping cart
    """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect('view_cart')
