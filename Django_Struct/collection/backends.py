from registration.backends.simple.views import RegistrationView
from collection.forms import MyRegistrationForm


# my new reg view, subclassing RegistrationView from our plugin
class MyRegistrationView(RegistrationView):
    form_class = MyRegistrationForm

    # the named URL that we want to redirect to after 
    # successful registration
    success_url = 'registration_create_project'

