from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


from quizsection.forms import *

# Create your views here.
 

def home(request):
    return render(request, 'quizsection/home.html')


def registerPage(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            # Save the form data
            user = form.save()
            username = form.cleaned_data.get('username')

            # messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    else:
        form = PersonForm()

    context = {'form': form}
    return render(request, 'quizsection/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # replace 'home' with the name of your homepage URL pattern
            return redirect('home')
    else:
        form = AuthenticationForm()

    context = {'form': form}

    return render(request, 'quizsection/login.html', context)
