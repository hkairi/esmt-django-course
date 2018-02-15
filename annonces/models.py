
from django.db import models
from django.utils.text import slugify
# Create your models here.


class Categorie(models.Model):
    titre = models.CharField(max_length=50)
    photo = models.ImageField(default='default.png', blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.titre


class Annonce(models.Model):
    titre = models.CharField(max_length=50)
    prix = models.CharField(max_length=10)
    photo = models.ImageField(default='default.jpg', blank=True)
    description = models.TextField(max_length=200, default='DESC')
    publiee = models.BooleanField(default=False)
    date_publication = models.DateField(auto_now_add=True)
    categorie = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, blank=False
    )
    slug = models.SlugField()

    def __str__(self):
        return self.titre

    def _get_unique_slug(self):
        slug = slugify(self.titre)
        unique_slug = slug
        num = 1
        while Annonce.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    @classmethod
    def publiees(cls):
        return cls.objects.filter(publiee=True).order_by('prix')

    @classmethod
    def liste_publiees(cls, catId):
        return cls.publiees().filter(categorie_id=catId)

    @classmethod
    def search(klass, query):
        if query == '':
            return []
        else:
            return klass.publiees().filter(titre__contains=query)
