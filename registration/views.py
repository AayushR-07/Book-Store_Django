from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import RegistrationForm
from .models import Registration


def registration_form(request):
    """Handle registration form display and submission"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            print("Success")
            return redirect('registration:form')
    else:
        form = RegistrationForm()

    return render(request, 'registration/form.html', {'form': form})