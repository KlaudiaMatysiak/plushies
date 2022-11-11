from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
        Form to allow users to contact site owner
    """
    class Meta:
        model = Contact
        fields = "__all__"
