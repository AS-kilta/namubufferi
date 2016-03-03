from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from .models import *
import datetime
import random
import hashlib
from .forms import *


# TODO: Remve unused
context = dict(backend_form=AuthenticationForm(),
               signin_form=AuthenticationForm(),
               register_form=UserCreationForm(),
               money_form=MoneyForm(),
               user_photos=[],
               browse_photos=[],
               products=Product.objects.all(),
               categories=Category.objects.all(),
               scroll_to="",
               money_message="",
               buy_message="",
               register_message="",
               permalink_key=""
               )


def cover(request):
    return render(request, 'namubufferiapp/base.html', context)


def register(request):
    """
    Check:
    http://www.djangobook.com/en/2.0/chapter14.html
    http://ipasic.com/article/user-registration-and-email-confirmation-django/
    https://docs.djangoproject.com/en/1.7/topics/email/

    """
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        context['register_form'] = register_form
        if register_form.is_valid():
            new_user = register_form.save()
            # Create a placeholder for a profile. Currently not in use.
            new_profile = UserProfile()
            new_profile.user = new_user
            new_profile.save()
            context['scroll_to'] = ""
            context['register_message'] = "You can now sign in with the account."

    return render(request, 'namubufferiapp/base.html', context)


def buy_view(request, product_key):
    price = 1  # TODO: Get price with product_key form products
    request.user.userprofile.make_payment(price)
    context['money_message'] = "1231233"
    return render(request, 'namubufferiapp/base.html', context)


def deposit_view(request, amount):
    if request.method == 'POST':
        money_form = MoneyForm(request.POST)
        context['money_form'] = money_form
    if money_form.is_valid():
        amount = request.POST['amount']
        request.user.userprofile.make_deposit(amount)
        context['scroll_to'] = ""
        context['register_message'] = "Money added"

    return render(request, 'namubufferiapp/base.html', context)
