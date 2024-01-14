from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def homepage(request):
    context = {'first_name': 'Jon', 'last_name': 'Doe'}
    return render(request, 'crm/index.html', context)

def task(request):

    context = {'allTasks': Task.objects.all()}

    return render(request, 'crm/task.html', context)

def clients(request):
    clientList = [
        {'id': 1, 'name': 'Jon Doe', 'occupation': 'carpenter', 'email': 'johndoe@hotmail.com'},
        {'id': 2, 'name': 'Jane Doe', 'occupation': 'plumber', 'email': 'jane@gmail.de'},
        {'id': 3, 'name': 'John Smith', 'occupation': 'electrician', 'email': 'john@libero.it'},
        {'id': 4, 'name': 'Jane Smith', 'occupation': 'carpenter', 'email': 'fidgety@smash.com'},
    ]

    context = {'clients': clientList}

    return render(request, 'crm/clients.html', context)

def register(request):
    return HttpResponse('This is the registration page')

def task_form(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/task')

    context = {'TaskForm': form}

    return render(request, 'crm/create-task.html', context)
