from django.db import models

# Create your models here.
class FilesUplaod(models.Model):
    file = models.FileField()