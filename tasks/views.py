from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.urls import reverse_lazy


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.id])


class TaskListView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/list.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/edit.html"
    fields = ["is_completed"]

    def get_success_url(self):
        return reverse_lazy("show_my_tasks")
