from django.shortcuts import render


def contact(request):
    """ A view of the Contact Page """
    return render(request, 'contact/contact.html')
