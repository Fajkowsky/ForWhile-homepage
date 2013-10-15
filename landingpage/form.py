from django import forms


class ContactForm(forms.Form):
    mail = forms.EmailField(widget=forms.TextInput(attrs=
        {'class': 'form-control input-lg',
        'title': 'Dont worry. We hate spam, and will not share your email with anyone',
        'placeholder': 'Enter your email address to',
        }), label='', error_messages={'invalid':'', 'required':''})
