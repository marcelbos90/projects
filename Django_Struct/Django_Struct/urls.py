from django.contrib import admin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include
from django.views.generic import TemplateView

from collection.backends import MyRegistrationView
from collection import views

urlpatterns = [
    # index
    path('', views.index, name='home'),

    # about and contact pages without a reference in view.py
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # project page on the basis of the slug
    path('projects/index', views.project_index, name='project_index'),

    path('projects/<slug>/', views.project_detail, name='project_detail'),
    path('projects/<slug>/edit/', views.edit_project, name='edit_project'),

    # password reset/recover feature
    path('accounts/password/reset/',
        PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
        name='password_reset'),
    path('accounts/password/reset/done/',
        PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    path('accounts/password/reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('accounts/password/done/',
        PasswordResetDoneView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),

    # additional registration page so when a new user signs up, they'll also set up their Project
    path('accounts/register/',
        MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/create_project/',
        views.create_project, name='registration_create_project'),

    # for any URL path starting with accounts/, search for an matching URL path in django-registratiom\n-redux URL's
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
]