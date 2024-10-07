from django.shortcuts import render
from adressformular.views import adressformular, adresse_speichern
from django.urls import path
from adressformular import views


urlpatterns = [
    path('adressformular/', views.adressformular, name='adressformular'),
    path('adressuebersicht/', views.adressuebersicht, name='adressuebersicht'),
    path('adresse_speichern/',views.adresse_speichern,name='adresse_speichern'),
]



