# Squeezelite Radiotasten

Kleines Python-Skript, um einen Drehimpulsgeber sowie 6 Taster per GPIO auszulesen und bei Betätigung Kommandos zum Logitech Media Server zu senden. So kann ein kleines simples WLAN-Radio mit Squeezelite aufgebaut werden, welches sich auch über Taster/Drehimpulsgeber steuern lässt.

Für den Drehimpulsgeber verwende ich die Encoder-Library von Neal Stansby: https://github.com/nstansby/rpi-rotary-encoder-python

Das Skript "radiotasten.py" überwacht die GPIOs und sendet entsprechende Befehle an das CLI des Logitech Media Sevrers (JSON).

Das Skript "watchdog.sh" überwacht, ob "radiotasten.py" noch läuft und startet es gegebenenfalls neu. Es sollte per cron regelmäßig aufgerufen werden.

Alle Einstellungen werden am Anfang des Skripts "radiotasten.py" durchgeführt.

Die Taster können gegen Ground oder gegen +3.3V verschaltet werden. Der Drehimpulsgeber *muss* gegen +3.3V verschaltet werden.

Beschreibung des gesamten Projekts findet sich im Loxwiki: https://www.loxwiki.eu/x/SoAuBQ
