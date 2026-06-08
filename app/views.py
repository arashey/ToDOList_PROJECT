from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, User
from .forms import TaskForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('date_time')
    return render(request, 'home.html', {'tasks':tasks})

@login_required
def task_details(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'home_details.html', {'task':task})

@login_required
def add_task(request):
    if request.method == 'POST':
        forms = TaskForm(request.POST)
        if forms.is_valid():
            task = forms.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        forms = TaskForm()
    
    return render(request, 'add_task.html', {'forms':forms})

@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        forms = TaskForm(request.POST, instance=task)
        if forms.is_valid():
            forms.save()
            return redirect('task_list')
    else:
        forms = TaskForm(instance=task)
    
    return render(request, 'add_task.html', {'forms':forms})

@login_required            
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    
    return render(request, 'task_delete.html', {'task':task})


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request,'رمز عبور همخوانی ندارد!')
        
        elif User.objects.filter(username=username).exists():
            messages.error(request, f"نام کاربری {username} قبلا وجود دارد!")
        
        else:
            user = User.objects.create_user(username=username, password=password1)
            login(request,user)
            return redirect('login')
    
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        
        else:
            messages.error(request, 'رمز عبور یا نام کاربری اشتباه است !')
    
    return render(request, 'login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')   
    