from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.urls import reverse_lazy
from django.views.generic.list import ListView


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.project.id])


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"
    fields = ["name", "start_date", "due_date", "is_completed"]

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/list.html"
    fields = ["is_completed"]

    def get_success_url(self):
        return reverse_lazy("show_my_tasks")
