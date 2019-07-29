from django.shortcuts import render, redirect

from collection.forms import ProjectForm
from collection.models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects,})

def project_detail(request, slug):
    # grab the object
    project = Project.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'projects/project_detail.html', {'project': project,})

def edit_project(request, slug):
    # grab the object
    project = Project.objects.get(slug=slug)

    # set the form we're using
    form_class = ProjectForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(data=request.POST, instance=project)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('project_detail', slug=project.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=project)

    # and render the template
    return render(request, 'projects/edit_project.html', {'project': project, 'form': form,})