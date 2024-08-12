from django import forms
from django.utils.translation import gettext_lazy as _
from portfolio.models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True, label=_("Your name"))
    email = forms.EmailField(required=True, label=_("Your email"))
    content = forms.CharField(
        widget=forms.Textarea, required=True, label=_("Your message")
    )

    class Meta:
        model = Contact
        fields = ("name", "email", "content")
