from django.shortcuts import render, redirect
from .models import Annonce, Categorie
from django.http import JsonResponse

from .formulaires import CreationAnnonce


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


def addAnnonce(request):
    formulaire = CreationAnnonce()
    context = {
        'formulaire': formulaire
    }

    if request.method == 'POST':
        formulaire = CreationAnnonce(request.POST, request.FILES)
        if formulaire.is_valid():
            annonce = Annonce(**formulaire.cleaned_data)
            annonce.save()
            return redirect('annonces:details', id=annonce.id)
    else:
        return render(request, "addAnnonce.html", context)


def api(request):
    return JsonResponse({'annonces': []})
