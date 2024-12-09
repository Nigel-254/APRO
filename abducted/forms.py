from .models import *
from django import forms
from .models import UserProfile


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password before saving
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )


class MissingPersonReportForm(forms.ModelForm):
    class Meta:
        model = MissingPersonReport
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Username'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Phone Number'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lost person name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Height in cm (optional)'}),
            'physical_details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe any physical details (optional)', 'rows': 5}),
            'date_of_disappearance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location_of_disappearance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'contact_details': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional comments', 'rows': 3}),
            'images': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name'

    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'

    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your phone number'

    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your message'
    }))


# Form for FoundPerson Model
class FoundPersonForm(forms.ModelForm):
    class Meta:
        model = FoundPerson
        fields = ['your_name', 'phone_number', 'email', 'found_person_name', 'location']
        widgets = {
            'your_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'found_person_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the found person'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
        }