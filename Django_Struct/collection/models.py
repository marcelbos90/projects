from django.db import models

import uuid

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    uid = str(uuid.uuid4())

class WorkPackage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    number = models.IntegerField()