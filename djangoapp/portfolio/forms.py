from django import forms
from portfolio.models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Contact
        fields = ("name", "email", "content")
