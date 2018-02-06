from django.db import models

# Create your models here.
class Annonce(models.Model):
    titre = models.CharField(max_length=50)
    description = models.TextField(max_length=200, default='DESC')
    publiee = models.BooleanField(default=False)

