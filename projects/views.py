from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = "projects/list.html"
