from django.shortcuts import render
from .models import Annonce
def index(request):
    context = {
        'annonces': Annonce.objects.all()
    }
    return render(request, "index.html", context)
