from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)

# Create your models here.
