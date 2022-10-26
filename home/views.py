from django.shortcuts import render


def index(request):
    """ A view of the Home Page """
    return render(request, 'home/index.html')
