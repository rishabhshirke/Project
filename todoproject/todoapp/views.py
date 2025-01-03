from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

# from django.views.decorators.cache import cache_page


# Create Task
def create_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST.get("description", "")
        Task.objects.create(title=title, description=description)
        return redirect("task_list")
    return render(request, "todoapp/create_task.html")


# Read Tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "todoapp/task_list.html", {"tasks": tasks})


# Update Task
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.title = request.POST["title"]
        task.description = request.POST.get("description", "")
        task.completed = "completed" in request.POST
        task.save()
        return redirect("task_list")
    return render(request, "todoapp/update_task.html", {"task": task})


# Delete Task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("task_list")


# Create your views here.
# @cache_page(60 * 15)
# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, "todoapp/task_list.html", {"tasks": tasks})


# def add_task(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         Task.objects.create(title=title)
#         return redirect("task_list")
#     return render(request, "todoapp/add_task.html")


# def delete_task(reuqest, task_id):
#     task = Task.objects.get(id=task_id)
#     task.delete()
#     return redirect("task_list")
