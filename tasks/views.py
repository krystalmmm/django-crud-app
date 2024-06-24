from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task
from .forms import TaskForm

# Create your views here.

# Create a task
def task_create(request):
  # If user uses POST method, then get the posted data using request.POST
  if request.method == "POST":
    # Bind user data with TaskForm
    form = TaskForm(request.POST)
    # Form authentication, if form is valid, then save the data into database
    if form.is_valid():
      form.save()
      # Redirect to task list
      return redirect(reverse("tasks:task_list"))
  else:
    # Else, empty form
    form = TaskForm()
  return render(request, "tasks/task_form.html", { "form": form, })
    

# Retrieve task list
def task_list(request):
  # Get task list from database
  tasks = Task.objects.all()
  # Get the right template to render data and pass the data
  return render(request, "tasks/task_list.html", { "tasks": tasks, })
  

# Retrieve single task
def task_detail(request, pk):
  # Get the pk value of a single task from url, then search in database to get the single task
  task = get_object_or_404(Task, pk=pk)
  return render(request, "tasks/task_detail.html", { "task": task, })


# Update a task
def task_update(request, pk):
  # Get the pk value of a single task from url, then search in database to get the task
  task_obj = get_object_or_404(Task, pk=pk)
  if request.method == "POST":
    form = TaskForm(instance=task_obj, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect(reverse("tasks:task_detail", args=[pk,]))
  else:
    form = TaskForm(instance=task_obj)
  return render(request, "tasks/task_form.html", { "form": form, "object": task_obj })


# Delete a task
def task_delete(request, pk):
  # Get the pk value of a single task from the url, then search in database to get this task
  task_obj = get_object_or_404(Task, pk=pk)
  task_obj.delete() # Delete and redirect
  return redirect(reverse("tasls:task_list"))
