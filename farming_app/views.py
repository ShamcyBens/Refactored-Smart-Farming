from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseBadRequest
from django.contrib import messages
from datetime import date
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib import messages, auth
import datetime
from re import split
from django.http import FileResponse
import io
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

def home(request):
    
    return render(request,'home.html')

def dashboard(request):
    
    return render(request,'dashboard.html')

def farmerregister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration successful. You can now login.')
            return redirect('login')
                    
    else:
        form = RegistrationForm()
    
    context = {
        'form': form
    }
    return render(request,'register.html', context)


def join_group(request):
    return render(request, 'proceed.html')

def specific_join_group(request):
    return render(request, 'join_group.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)  # Use the renamed auth_login function
            current_user = Account.objects.get(id=request.user.id)
            if not farmer.objects.filter(user=current_user).exists():
                farmer = farmer(user=current_user)
                farmer.save()

            return redirect('create_group')

        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'login.html')



@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('home')


def farm_form_view(request):
    if request.method == 'POST':
        form = FarmForm(request.POST, request.FILES)
        if form.is_valid():

            farm = form.save(commit=False)
            farm.user = request.user.userprofile  # Assuming you have a UserProfile linked to your User model
            farm.save()
            return redirect('farm_detail', pk=farm.pk)  # Redirect to the farm detail page
    else:
        form = FarmForm()

    return render(request, 'farm.html', {'form': form})



def crop_form_view(request):
    if request.method == 'POST':
        form = CropForm(request.POST, request.FILES)
        if form.is_valid():
            crop = form.save(commit=False)
            crop.user = request.user.userprofile  
            crop.save()
            return redirect('crop_detail', pk=farm.pk) 
    else:
        form = CropForm()

    return render(request, 'crop.html', {'form': form})


def harvest_form_view(request):
    if request.method == 'POST':
        form = HarvestForm(request.POST, request.FILES)
        if form.is_valid():
            harvest = form.save(commit=False)
            harvest.user = request.user.userprofile  
            harvest.save()
            return redirect('harvest_detail', pk=farm.pk) 
    else:
        form = HarvestForm()

    return render(request, 'harvest.html', {'form': form})


def daily_update_form_view(request):
    if request.method == 'POST':
        form = DailyUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            daily_update = form.save(commit=False)
            daily_update.user = request.user.userprofile  
            daily_update.save()
            return redirect('daily_update_detail', pk=farm.pk) 
    else:
        form = DailyUpdateForm()

    return render(request, 'daily_update.html', {'form': form})


def weather_data_form_view(request):
    if request.method == 'POST':
        form = WeatherDataForm(request.POST, request.FILES)
        if form.is_valid():
            weather_data = form.save(commit=False)
            weather_data.user = request.user.userprofile  
            weather_data.save()
            return redirect('weather_data_detail', pk=farm.pk) 
    else:
        form = WeatherDataForm()

    return render(request, 'weather_data.html', {'form': form})


def fertilizer_form_view(request):
    if request.method == 'POST':
        form = FertilizerForm(request.POST, request.FILES)
        if form.is_valid():
            fertilizer = form.save(commit=False)
            fertilizer.user = request.user.userprofile  
            fertilizer.save()
            return redirect('fertilizer_detail', pk=farm.pk) 
    else:
        form = FertilizerForm()

    return render(request, 'fertilizer.html', {'form': form})


def soil_form_view(request):
    if request.method == 'POST':
        form = SoilForm(request.POST, request.FILES)
        if form.is_valid():
            soil = form.save(commit=False)
            soil.user = request.user.userprofile  
            soil.save()
            return redirect('soil_detail', pk=farm.pk) 
    else:
        form = SoilForm()

    return render(request, 'soil.html', {'form': form})


def proceed(request):
    
    return render(request,'proceed.html')


def create_group(request):
    
    return render(request,'create_group/create_group.html')