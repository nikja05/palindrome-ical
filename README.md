# palindrome-ical
Dieses Skript nimmt alle Proben aus dem Intern Probenplan und packt sie in eine iCal Datei.
Du kannt diese iCal Datei dann in einen beliebigen Kalender laden.

## Schritt 0 - Den Code speichern.
Über den Dateien findest du einen grünen Knopf: 'Code'. Wenn du draufdrückst, gibt es die Möglichkeit, alles als .zip Datei herunterzuladen (unterster Knopf). Speichere die Datei am besten im Ordner 'Desktop'.


Danach musst du den Inhalt 'extrahieren'. Drücke dafür mit dem Rechtsklick auf den Ordner und suche die Option 'Alles extrahieren...'. Dies wird ein neues Fenster mit dem extrahierten Ordner öffnen. Wir werden von nun an damit arbeiten.

## Schritt 1 - Python herunterladen
Unter https://www.python.org/downloads/ findest du das Programm um Python zu installieren.

## Schritt 2 - main.py ausführen
Im Ordner [code](./code/) findest du die Datei main.py. Rechtsklick irgendwo im Ordner und wähle 'im Terminal öffnen'. Ein neues Fenster öffnet sich, dies ist das Terminal. 


Schreibe nun ```python main.py``` in die Kommandozeile (dort wo der Zeiger blink) und drücke Enter.
Das Programm wird ausgeführt, folge den Anweisungen: Gib deine mygymer E-Mail, dein Passwort und dein Betriebssystem (MAC oder Windows) ein.

Du wirst eine .ical Datei im Ordner [code/Mein Probenplan/](./code/Mein\ Probenplan/] finden. 

## Schritt 3 - .ical Datei in Kalender einfügen

### iCloud

### Google Kalender
1. Melde dich an im [Google Kalender](https://calendar.google.com/).
2. Drücke auf das Zahnrad in der oberen Leiste, danach 'Einstellungen'.
3. Drücke auf 'Importieren & Exportieren'
4. Du kannst nun die .ical Datei aus dem Ordner [Mein Probenplan/](./code/Mein\ Probenplan/] auswählen und somit den Kalender importieren.

## Gebrauchte Module und Link zur Dokumentation
- [icalendar](https://icalendar.readthedocs.io/en/latest/)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [selenium](https://selenium-python.readthedocs.io/)
- [beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)	
