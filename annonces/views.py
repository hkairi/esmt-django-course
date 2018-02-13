from django.shortcuts import render
from .models import Annonce, Categorie

from django.http import JsonResponse

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
    _annonces = Annonce.liste_publiees(catId)
    context = {
        'categorie': Categorie.objects.get(id=catId),
        'annonces': _annonces,
        'annonces_count': len(_annonces)
    }
    return render(request, "show-categorie.html", context)


def search(request):
    query = request.GET.get('query', '')
    context = {
        'annonces': Annonce.search(query)
    }
    return render(request, "results.html", context)


def api(request):
    return JsonResponse({'annonces': []})
