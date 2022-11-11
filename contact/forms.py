from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
        Form to allow users to contact site owner
    """
    class Meta:
        model = Contact
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove auto generated labels,
        set autofocus on full name field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['required'] = 'required'
            self.fields[field].label = False
