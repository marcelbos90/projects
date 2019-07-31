from django.contrib.auth.decorators import login_required
from django.http import Http404

from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from collection.forms import ProjectForm, MyRegistrationForm
from collection.models import Project

# Create your views here.
def index(request):
    return render(request, 'index.html',)

def project_index(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'projects/project_index.html', {'projects': projects,})

@login_required
def project_detail(request, slug):
    # grab the object
    project = Project.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'projects/project_detail.html', {'project': project,})

@login_required
def edit_project(request, slug):
    # grab the object
    project = Project.objects.get(slug=slug)

    # make sure the loggid user us the owner of the project
    if project.user != request.user:
        raise Http404

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

@login_required
def create_project(request):
    form_class = ProjectForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply the form
        form = form_class(request.POST)

        if form.is_valid():
            # create an instance but don't save yet
            project = form.save(commit=False)

            # set the additional details
            project.user = request.user
            project.slug = slugify(project.name)

            # save the object
            project.save()

            # redirect to our newly created project
            return redirect('project_detail', slug=project.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'projects/create_project.html', {'form': form,})

# https://stackoverflow.com/questions/15774127/django-registration-how-to-make-account-creation-ask-for-first-last-name
def register(sender, user, request, **kwargs):
    """
    Called via signals when user registers. Creates different profiles and
    associations
    """
    form_class = MyRegistrationForm(request.Post)
    # Update first and last name for user
    user.first_name=form.data['first_name']
    user.last_name=form.data['last_name']
    user.save()

    user_registered.connect(user_created)