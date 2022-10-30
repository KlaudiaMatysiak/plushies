from django.shortcuts import render, redirect, reverse


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

