from django import forms
from .models import NewsletterUser, Newsletter


class NewsletterUserForm(forms.ModelForm):

    class Meta:
        model = NewsletterUser
        fields = ["email"]


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ("body", "email", "name", "subject")
