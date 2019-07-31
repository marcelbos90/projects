from django.forms import ModelForm
from collection.models import Project
from registration.forms import RegistrationForm
from django.contrib.auth.models import User

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description',)

class MyRegistrationForm(RegistrationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'username', 'password1', 'password2',]
