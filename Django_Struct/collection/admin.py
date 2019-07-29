from django.contrib import admin

# Register your models here.
from collection.models import Project

# set up automated slug creation
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'description', 'uid')
    

# and register it
admin.site.register(Project, ProjectAdmin)