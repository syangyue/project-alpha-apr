from tasks.views import TaskCreateView, TaskListView, TaskUpdateView
from django.urls import path


urlpatterns = [
    path("create/", TaskCreateView.as_view(), name="create_task"),
    path("mine/", TaskListView.as_view(), name="show_my_tasks"),
    path("<int:pk>/complete/", TaskUpdateView.as_view(), name="complete_task"),
]
