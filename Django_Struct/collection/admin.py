from django.contrib import admin

# Register your models here.
from collection.models import Project, WorkPackage

# set up automated slug creation
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'description', 'uid')
    prepopulated_fields = {'slug': ('name',)}


class WorkPackageAdmin(admin.ModelAdmin):
    model = WorkPackage
    list_display = ('name', 'description')
    

# and register it
admin.site.register(Project, ProjectAdmin)
admin.site.register(WorkPackage, WorkPackageAdmin)