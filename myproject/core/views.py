from django.shortcuts import render
from .models import Contacto, Subscription
from .forms import ContactForm, SubscriptionForm
import time
# Create your views here.

def base(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        time.sleep(0.5)
        form = ContactForm()
    subscription = SubscriptionForm(request.POST or None)
    if subscription.is_valid():
        subscription.save()
        time.sleep(0.5)
        subscription = SubscriptionForm()
    context = {
        'form': form,
        'subscription': subscription,
    }
    return render(request, 'base.html', context)
