from django.db import models
from django.utils import timezone

class Adresse(models.Model):
    strasse = models.CharField(max_length=255)  # Textfeld für Straße
    hausnummer = models.CharField(max_length=10)  # Textfeld für Hausnummer (kann auch Zeichen wie '1a' enthalten)
    plz = models.CharField(max_length=10)  # Textfeld für PLZ (da auch führende Nullen möglich sind)
    ort = models.CharField(max_length=100)  # Textfeld für Ort
    bundesland = models.CharField(max_length=100)  # Textfeld für Bundesland
    timestamp = models.DateTimeField(auto_now = True)  # Zeitstempel mit aktuellem Datum und Zeit als Standard

    def __str__(self):
        return f'{self.strasse} {self.hausnummer}, {self.plz} {self.ort}, {self.bundesland}'
