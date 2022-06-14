from django.db import models

# Create your models here.
class Repo(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.name