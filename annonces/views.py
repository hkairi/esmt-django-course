from django.shortcuts import render
from .models import Annonce, Categorie


def index(request):
    context = {
        'annonces': Annonce.objects.all(),
        'categories': Categorie.objects.all()
    }
    return render(request, "index.html", context)


def show(request, id):
    context = {
        'annonce': Annonce.objects.get(id=id)
    }
    return render(request, "show.html", context)


def categorie(request, catId):
    context = {
        'categorie': Categorie.objects.get(id=catId),
        'annonces': Annonce.objects.filter(categorie_id=catId, publiee=True)
    }
    return render(request, "show-categorie.html", context)
