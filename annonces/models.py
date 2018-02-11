from django.db import models

# Create your models here.


class Categorie(models.Model):
    titre = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.titre


class Annonce(models.Model):
    titre = models.CharField(max_length=50)
    description = models.TextField(max_length=200, default='DESC')
    publiee = models.BooleanField(default=False)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.titre
