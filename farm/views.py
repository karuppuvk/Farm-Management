from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import (
    RegisterForm, CropForm, LivestockForm, FinancialForm,
    WorkerForm, TaskForm, WeatherForm
)
from .models import Crop, Livestock, FinancialRecord, Worker, Task, Weather


def home_view(request):
    return render(request, 'farm/index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'farm/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'farm/login.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'farm/register.html', {'form': form})


@login_required
def dashboard(request):
    crop_form = CropForm(request.POST or None, prefix='crop')
    livestock_form = LivestockForm(request.POST or None, prefix='livestock')
    financial_form = FinancialForm(request.POST or None, prefix='financial')
    worker_form = WorkerForm(request.POST or None, prefix='worker')
    task_form = TaskForm(request.POST or None, prefix='task')
    weather_form = WeatherForm(request.POST or None, prefix='weather')

    if request.method == 'POST':
        if 'submit_crop' in request.POST and crop_form.is_valid():
            crop_form.save()
            return redirect('view_data')
        elif 'submit_livestock' in request.POST and livestock_form.is_valid():
            livestock_form.save()
            return redirect('view_data')
        elif 'submit_financial' in request.POST and financial_form.is_valid():
            financial_form.save()
            return redirect('view_data')
        elif 'submit_worker' in request.POST and worker_form.is_valid():
            worker_form.save()
            return redirect('view_data')
        elif 'submit_task' in request.POST and task_form.is_valid():
            task_form.save()
            return redirect('view_data')
        elif 'submit_weather' in request.POST and weather_form.is_valid():
            weather_form.save()
            return redirect('view_data')

    return render(request, 'farm/dashboard.html', {
        'crop_form': crop_form,
        'livestock_form': livestock_form,
        'financial_form': financial_form,
        'worker_form': worker_form,
        'task_form': task_form,
        'weather_form': weather_form,
    })


# @login_required
# def dashboard_view(request):
#     context = {
#         'crops': Crop.objects.all(),
#         'livestock': Livestock.objects.all(),
#         'financials': FinancialRecord.objects.all(),
#         'workers': Worker.objects.all(),
#         'tasks': Task.objects.all(),
#         'weather': Weather.objects.all(),
#     }
#     return render(request, 'farm/main_dashboard.html', context)
# the above one is not working

def logout_view(request):
    logout(request)
    return redirect('index')

# i add this
def view_data(request):
    context = {
        'crops': Crop.objects.all(),
        'livestock': Livestock.objects.all(),
        'financials': FinancialRecord.objects.all(),
        'workers': Worker.objects.all(),
        'tasks': Task.objects.all(),
        'weather': Weather.objects.all(),
    }
    return render(request, 'farm/view_data.html', context)
