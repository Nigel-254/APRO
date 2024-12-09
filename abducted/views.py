from itertools import zip_longest

from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, MissingPersonReportForm, ContactForm, FoundPersonForm
from .models import UserProfile, MissingPersonReport, ContactDetails, FoundPerson


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # This automatically hashes the password
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('report missing person')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def about(request):
    return render(request, 'about.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            ContactDetails.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def published(request):
    reports = MissingPersonReport.objects.all()
    return render(request, 'published.html', {'reports': reports})

def administration(request):
    missing = MissingPersonReport.objects.all()
    # Calculate total cases
    total_cases = missing.count()
    # Pass the combined data to the template
    return render(request, 'administration.html', {'total_cases': total_cases, 'missing': missing})


# @login_required
def report(request):
    if request.method == 'POST':
        form = MissingPersonReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Report submitted successfully!')
            return redirect('report missing person')
        else:
            messages.error(request, 'There was an error submitting the report. Please try again.')
    else:
        form = MissingPersonReportForm()

    return render(request, 'report.html', {'form': form})


def found(request):
    # Get all FoundPerson objects
    found_persons = FoundPerson.objects.all()

    total_found = found_persons.count()

    if request.method == "POST":
        form = FoundPersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Details about the found person have been submitted successfully!")
            return redirect('found cases')  # Redirect to the same page or another view
        else:
            messages.error(request, "There was an error. Please check the details and try again.")
    else:
        form = FoundPersonForm()

    return render(request, 'found.html', {'form': form, 'total_found': total_found})

# Custom admin view for displaying both tables
def message(request):
    contact_details = ContactDetails.objects.all()  # Get all ContactDetails
    found_persons = FoundPerson.objects.all()  # Get all FoundPerson objects
    return render(request, 'messages.html', {
        'contact_details': contact_details,
        'found_persons': found_persons
    })


def edit(request, id):
    missing = get_object_or_404(MissingPersonReport, id=id)

    form = MissingPersonReportForm(request.POST or None, request.FILES or None, instance=missing)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Missing person updated successfully.')
        return redirect('administration')
    return render(request, 'edit.html', {'form': form, 'missing': missing})


def delete(request, id):
    student = get_object_or_404(MissingPersonReport, id=id)
    try:
        student.delete()
        messages.success(request, 'Student deleted successfully.')

    except Exception as e:
        messages.error(request, 'student not deleted.')
    return redirect('administration')