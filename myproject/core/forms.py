from django import forms
from .models import Contacto, Subscription

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['name', 'mail', 'subject', 'description']



class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['mail', 'start_date', 'end_date']
