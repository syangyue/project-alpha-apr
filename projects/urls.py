from .views import ProjectListView, ProjectDetailView, ProjectCreateView
from django.urls import include, path


urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="show_project"),
    path("create/", ProjectCreateView.as_view(), name="create_project"),
]
