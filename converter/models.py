from django.db import models
import os

# Create your models here.
class FilesUplaod(models.Model):
    file = models.FileField()

    def filename(self):
        return os.path.basename(self.file.name)