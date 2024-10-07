from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import AdresseForm
from .models import Adresse
from django.contrib import messages
from django.http import JsonResponse
from .forms import AdresseForm

def adressformular(request):
    if request.method == 'POST':
        form = AdresseForm(request.POST)
        if form.is_valid():
            form.save()  # Speichert die Adresse in der Datenbank
            return redirect('adressuebersicht')  # Erfolgsweiterleitung nach dem Speichern
    else:
        form = AdresseForm()

    return render(request, 'adressformular.html', {'form': form})

def adressuebersicht(request):
    addresses = Adresse.objects.all()  # Alle Adressen aus der Datenbank abrufen
    return render(request, 'adressuebersicht.html', {'addresses': addresses})



def adresse_speichern(request):
    if request.method == 'POST':
        form = AdresseForm(request.POST)
        if form.is_valid():
            form.save()  # Adresse speichern
            return JsonResponse({'success': True, 'message': 'Adresse wurde erfolgreich gespeichert!'})  # Erfolgsmeldung
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)  # Fehler zurückgeben
    return JsonResponse({'success': False}, status=405)  # Methode nicht erlaubt
