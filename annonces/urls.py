from django.urls import path
from . import views

app_name = 'annonces'

urlpatterns = [
    path('', views.index),
    path('search', views.search, name='search'),
    path('categories/<int:catId>/annonces', views.categorie, name='categorie'),
    path('annonces/', views.index),
    path('annonces/<int:id>', views.show, name='details'),
    path('annonces/new', views.addAnnonce, name='addAnnonce'),
]
