from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from collection import views

urlpatterns = [
    # index
    path('', views.index, name='home'),

    # about and contact pages without a reference in view.py
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # project page on the basis of the slug
    path('projects/<slug>/', views.project_detail, name='project_detail'),
    path('projects/<slug>/edit/', views.edit_project, name='edit_project'),


    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]