from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Task, User
from .forms import TaskForm, LoginForm
from django.db.models import Q

# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'task_tracker/task_list.html', {'tasks': tasks})

def task_list(request):
    query = request.GET.get('q')
    sort_by = request.GET.get('sort_by', 'title')

    if query:
        tasks = Task.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).order_by(sort_by)
    else:
        tasks = Task.objects.all().order_by(sort_by)

    context = {
        'tasks': tasks,
        'sort_by': sort_by,
        'query': query
    }
    return render(request, 'task_tracker/task_list.html', context)

def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task_tracker:task_list')
    return render(request, 'task_tracker/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_tracker:task_list')
    return render(request, 'task_tracker/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_tracker:task_list')
    return render(request, 'task_tracker/task_confirm_delete.html', {'task': task})

from .models import Task, User
from .forms import TaskForm, LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = authenticate(request, username=username)
            if user is not None:
                login(request, user)
                request.session['user_id'] = user.id
                return redirect('task_tracker:task_list')
    else:
        form = LoginForm()
    return render(request, 'task_tracker/login.html', {'form': form})