from tasks.views import TaskCreateView
from django.urls import path


urlpatterns = [
    path("create/", TaskCreateView.as_view(), name="create_task")
]
