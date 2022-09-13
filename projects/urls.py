from .views import ProjectListView
from django.urls import include, path


urlpatterns = [
    path('', ProjectListView.as_view(), name="list_projects"),
]
