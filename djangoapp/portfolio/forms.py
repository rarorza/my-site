from django import forms
from portfolio.models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True, label="Your name")
    email = forms.EmailField(required=True, label="Your email")
    content = forms.CharField(
        widget=forms.Textarea, required=True, label="Your message"
    )

    class Meta:
        model = Contact
        fields = ("name", "email", "content")
