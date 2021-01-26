from django.shortcuts import render
from projects.models import Project


# Create your views here.
def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})


def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/project.html', {'project': project})

