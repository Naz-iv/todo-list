from django.shortcuts import render
from django.views import generic

from todo.models import Task


class TaskListView(generic.ListView):
    model = Task
