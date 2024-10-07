
# Interaktives Adressformular mit Django

Dies ist ein interaktives Adressformular-Projekt mit Django, das es ermöglicht, Adressen einzugeben, zu speichern und eine Übersicht der gespeicherten Adressen anzuzeigen. Das Projekt verwendet externe APIs für Straßendaten und bietet eine benutzerfreundliche Oberfläche für die Verwaltung von Adressen.

## Projektübersicht

### Aufgabenstellung

- Ein interaktives Formular für Adressdaten implementieren.
- Speicherung und Anzeige von Adressen über ein Django-Backend.
- Verwendung der Wiener Adressservice API für Straßenvorschläge.
- Frontend-Validierung und Benutzerführung mit JavaScript.
- Styling mit CSS für ein responsives und sauberes Design.

### Funktionen

1. **Adressformular**:
   - Eingabefelder für Straße, Hausnummer, PLZ, Ort und Bundesland.
   - Vorschläge für Straßen, basierend auf Benutzereingaben, unter Verwendung der Wiener Adressservice API.
   
2. **Adressübersicht**:
   - Zeigt eine Liste der gespeicherten Adressen an.
   - Zeitstempel für jede Adresse wird mit angezeigt.

3. **API-Integration**:
   - Verwendung von `fetch()` zum Abrufen von Straßenvorschlägen und Speichern der Adresseingaben über einen API-Endpunkt.

4. **Benutzerfreundliche Fehlerbehandlung**:
   - Fehlermeldungen werden im Formular angezeigt, wenn Eingaben ungültig sind.
   - Bei Erfolg wird eine Meldung angezeigt, ohne die Seite neu zu laden.

## Installation und Ausführung

### Voraussetzungen

- Python 3.x
- Django
- Git

### Schritte zur Installation

1. Klone das Repository:
   ```bash
   git clone https://github.com/maximiliankraft/wieneradressen.git
   ```
   
2. Navigiere in das Projektverzeichnis:
   ```bash
   cd wieneradressen
   ```

3. Erstelle eine virtuelle Umgebung und aktiviere sie:
   ```bash
   python -m venv env
   source env/bin/activate   # Linux/macOS
   env\Scripts\activate      # Windows
   ```

4. Installiere die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

5. Erstelle die Datenbank:
   ```bash
   python manage.py migrate
   ```

6. Starte den lokalen Server:
   ```bash
   python manage.py runserver
   ```

7. Öffne die Anwendung im Browser unter `http://localhost:8000`.

### Projektstruktur

```bash
wieneradressen/
│
├── adressformular/
│   ├── migrations/             # Datenbankmigrationen
│   ├── models.py               # Adressmodell
│   ├── views.py                # Backend-Logik
│   ├── urls.py                 # URL-Routing
│   ├── templates/              # HTML-Templates für Formulare und Übersicht
│   └── static/                 # CSS und JavaScript Dateien
│
├── wieneradressen/
│   ├── settings.py             # Django-Projekteinstellungen
│   └── urls.py                 # Haupt-URL-Konfiguration
│
└── README.md                   # Diese Datei
```

## Funktionen im Detail

### 1. Modell: Adresse
Das Modell `Adresse` in `models.py` speichert folgende Felder:

- Straße
- Hausnummer
- PLZ
- Ort
- Bundesland
- Zeitstempel der Eingabe

### 2. Views

- **`adressformular`:** Rendert das Formular zur Adresseingabe.
- **`adresse_speichern`:** Verarbeitet die Formularanfragen und speichert Adressen via AJAX.
- **`adressen_anzeigen`:** Stellt alle gespeicherten Adressen in einer Tabelle dar.

### 3. JavaScript-Implementierung

Die Datei `adressService.js` enthält:

- Funktionen, um Straßenvorschläge von der Wiener Adressservice API zu holen und diese anzuzeigen.
- Fehlerbehandlung und Feedback-Funktionen für den Benutzer.






