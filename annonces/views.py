from django.shortcuts import render
from .models import Annonce


def index(request):
    context = {
        'annonces': Annonce.objects.all()
    }
    return render(request, "index.html", context)


def show(request, id):
    context = {
        'annonce': Annonce.objects.get(id=id)
    }
    return render(request, "show.html", context)
