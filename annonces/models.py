from django.db import models

# Create your models here.


class Categorie(models.Model):
    titre = models.CharField(max_length=50)
    photo = models.ImageField(default='default.png', blank=True)
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

    @classmethod
    def publiees(cls):
        return cls.objects.filter(publiee=True).order_by('titre')

    @classmethod
    def liste_publiees(cls, catId):
        return cls.publiees().filter(categorie_id=catId)

    @classmethod
    def search(klass, query):
        if query == '':
            return []
        else:
            return klass.publiees().filter(titre__contains=query)
