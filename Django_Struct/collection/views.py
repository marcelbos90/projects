from django.shortcuts import render
from collection.models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects,})

def project_detail(request, uid):
    # grab the object
    project = Project.objects.get(uid=uid)

    # and pass to the template
    return render(request, 'projects/project_detail.html', {'project': project,})