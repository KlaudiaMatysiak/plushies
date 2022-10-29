from django.shortcuts import render


def view_cart(request):
    """ A view of the cart contents """
    return render(request, 'cart/cart.html')
