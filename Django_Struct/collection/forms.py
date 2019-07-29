from django.forms import ModelForm

from collection.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description',)
