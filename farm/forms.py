from django import forms
from django.contrib.auth.models import User
from .models import Crop, Livestock, FinancialRecord, Worker, Task, Weather

# User registration form
class RegisterForm(forms.ModelForm):
    full_name = forms.CharField(
        label="Full Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your full name',
            'id': 'id_full_name'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a secure password',
            'id': 'id_password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a username'}),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters.")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['full_name']
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = '__all__'
        widgets = {
            'planting_date': forms.DateInput(attrs={'type': 'date'}),
            'harvest_date': forms.DateInput(attrs={'type': 'date'}),
        }


class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = ['type', 'count']

class FinancialForm(forms.ModelForm):
    class Meta:
        model = FinancialRecord
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'scheduled_date': forms.DateInput(attrs={'type': 'date'}),
        }


class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = '__all__'
        widgets = {
            'forecast_date': forms.DateInput(attrs={'type': 'date'}),
        }
