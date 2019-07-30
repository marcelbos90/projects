from django.contrib.auth.models import User
from django.db import models

import uuid

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    uid = str(uuid.uuid4())

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    

class WorkPackage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    number = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)