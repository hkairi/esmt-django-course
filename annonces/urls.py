from django.urls import path
from . import views

app_name = 'annonces'

urlpatterns = [
    path('', views.index),
    path('annonces/<int:id>', views.show, name='details'),
]
