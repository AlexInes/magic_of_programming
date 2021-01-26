from projects import views
from django.urls import path

app_name = "projects"

urlpatterns = [
    path('', views.projects_list, name="projects"),
    path('<int:pk>', views.project_details, name="project_details")
]
