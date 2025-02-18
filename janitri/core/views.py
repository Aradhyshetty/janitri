from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
import os
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, HeartRate
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def add_patient(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        contact = request.POST["contact"]
        patient = Patient.objects.create(user=request.user, name=name, age=age, contact=contact)
        return redirect("dashboard")
    return render(request, "add_patient.html")

@login_required
def record_heart_rate(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if request.method == "POST":
        rate = request.POST["rate"]
        HeartRate.objects.create(patient=patient, rate=rate)
        return redirect("dashboard")
    return render(request, "record_heart_rate.html", {"patient": patient})

@login_required
def get_heart_rates(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    heart_rates = HeartRate.objects.filter(patient=patient).values()
    return JsonResponse(list(heart_rates), safe=False)
