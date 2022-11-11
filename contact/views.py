from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """ A view of the Contact Page """
    contact_form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thanks for your message!')
            contact_form = ContactForm()
    context = {
        'form': contact_form,
    }
    return render(request, 'contact/contact.html', context)
