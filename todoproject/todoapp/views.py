from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.views.decorators.cache import cache_page


# Create your views here.
# @cache_page(60 * 15)
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "todoapp/task_list.html", {"tasks": tasks})


def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(title=title)
        return redirect("task_list")
    return render(request, "todoapp/add_task.html")


def delete_task(reuqest, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("task_list")
