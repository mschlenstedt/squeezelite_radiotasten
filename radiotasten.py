#!/usr/bin/env python2

import RPi.GPIO as GPIO
from encoder import Encoder
import time
import os

#
# Einstellungen
#

# GPIO-Bezeichnungen (BCM) im Skript verwenden
GPIO.setmode(GPIO.BCM)

# LMS Einstellungen
# Player, der mit den Tasten gesteuert werden soll
player = "02:a7:37:bc:bd:1d"
# Host Deines Logitech Media Server (oder IP-Adresse)
server = "192.168.3.213"
# Port am LMS für CLI Kommandos
port = "9000"

# GPIO-Pins Drehimpulsgeber - gemeinsamer PIN auf +3.3V
in_a = 17
in_b = 27

# GPIO-Pins Pushbutton - wahlweise gegen GND oder +3.3V
in_c = 23
in_d = 24
in_e = 25
in_f = 8
in_g = 7
in_h = 6

# LMS Kommandos Drehimpulsgeber
# Links: Vol -5%
cmd_a = "curl -s -H \"Content-Type: application/json\" -X POST -d '{\"id\":1,\"method\":\"slim.request\",\"params\":[\"" + player + "\", [\"mixer\",\"volume\",\"+5\"]]}' http://" + server + ":" + port + "/jsonrpc.js"
# Rechts: Vol +5%
cmd_b = "curl -s -H \"Content-Type: application/json\" -X POST -d '{\"id\":1,\"method\":\"slim.request\",\"params\":[\"" + player + "\", [\"mixer\",\"volume\",\"-5\"]]}' http://" + server + ":" + port + "/jsonrpc.js"

# LMS Kommandos Pushbuttons
# Play Favorit 1 (Liste startet mit 0)
cmd_c = "curl -s -H \"Content-Type: application/json\" -X POST -d '{\"id\":1,\"method\":\"slim.request\",\"params\":[\"" + player + "\", [\"favorites\",\"playlist\",\"play\",\"item_id:0\"]]}' http://" + server + ":" + port + "/jsonrpc.js"
# Play Favorit 2
cmd_d = "curl -s -H \"Content-Type: application/json\" -X POST -d '{\"id\":1,\"method\":\"slim.request\",\"params\":[\"" + player + "\", [\"favorites\",\"playlist\",\"play\",\"item_id:1\"]]}' http://" + server + ":" + port + "/jsonrpc.js"
# Play Favorit 3
cmd_e = "curl -s -H \"Content-Type: application/json\" -X POST -d '{\"id\":1,\"method\":\"slim.request\",\"params\":[\"" + player + "\", [\"favorites\",\"playlist\",\"play\",\"item_id:2\"]]}' http://" + server + ":" + port + "/jsonrpc.js"
# Play Favorit 4
cmd_f = "curl -s -H \"Content-Type: application/json\" -X POST -d '{\"id\":1,\"method\":\"slim.request\",\"params\":[\"" + player + "\", [\"favorites\",\"playlist\",\"play\",\"item_id:3\"]]}' http://" + server + ":" + port + "/jsonrpc.js"
# Play Favorit 5
cmd_g = "curl -s -H \"Content-Type: application/json\" -X POST -d '{\"id\":1,\"method\":\"slim.request\",\"params\":[\"" + player + "\", [\"favorites\",\"playlist\",\"play\",\"item_id:4\"]]}' http://" + server + ":" + port + "/jsonrpc.js"
# Stop
cmd_h = "curl -s -H \"Content-Type: application/json\" -X POST -d '{\"id\":1,\"method\":\"slim.request\",\"params\":[\"" + player + "\", [\"mode\",\"stop\"]]}' http://" + server + ":" + port + "/jsonrpc.js"

# Pullup-/Pulldown-Widerstand einschalten
# Bei Verschaltung gegen GND: GPIO.PUD_UP
# Bei Verschaltung gegen +3.3V: GPIO.PUD_DOWN
pullupdown_in_c = GPIO.PUD_UP
pullupdown_in_d = GPIO.PUD_UP
pullupdown_in_e = GPIO.PUD_UP
pullupdown_in_f = GPIO.PUD_UP
pullupdown_in_g = GPIO.PUD_UP
pullupdown_in_h = GPIO.PUD_UP

# Bounce-Zeit in ms
bouncetime = 250

#
# Einstellungen Ende
#

# GPIO Settings
GPIO.setup(in_c, GPIO.IN, pull_up_down = pullupdown_in_c)
GPIO.setup(in_d, GPIO.IN, pull_up_down = pullupdown_in_d)
GPIO.setup(in_e, GPIO.IN, pull_up_down = pullupdown_in_e)
GPIO.setup(in_f, GPIO.IN, pull_up_down = pullupdown_in_f)
GPIO.setup(in_g, GPIO.IN, pull_up_down = pullupdown_in_g)
GPIO.setup(in_h, GPIO.IN, pull_up_down = pullupdown_in_h)

if pullupdown_in_c == GPIO.PUD_UP:
    edge_in_c = GPIO.FALLING
else:
    edge_in_c = GPIO.RISING

if pullupdown_in_d == GPIO.PUD_UP:
    edge_in_d = GPIO.FALLING
else:
    edge_in_d = GPIO.RISING

if pullupdown_in_e == GPIO.PUD_UP:
    edge_in_e = GPIO.FALLING
else:
    edge_in_e = GPIO.RISING

if pullupdown_in_f == GPIO.PUD_UP:
    edge_in_f = GPIO.FALLING
else:
    edge_in_f = GPIO.RISING

if pullupdown_in_g == GPIO.PUD_UP:
    edge_in_g = GPIO.FALLING
else:
    edge_in_g = GPIO.RISING

if pullupdown_in_h == GPIO.PUD_UP:
    edge_in_h = GPIO.FALLING
else:
    edge_in_h = GPIO.RISING

# Drehimpulsgeber
oldvalue = 0
def DIG1(value):
    global oldvalue
    if value > oldvalue:
        print str(value) + " -> Richtung ist rechts. Sende: "
        os.system(cmd_a)
        print ""
    if value < oldvalue:
        print str(value) + " -> Richtung ist links. Sende: "
        os.system(cmd_b)
        print ""
    oldvalue = value

# Button 1
def Button1(channel):
    print "Button 1 aktiviert. Sende:"
    os.system(cmd_c)
    print ""

# Button 2
def Button2(channel):
    print "Button 2 aktiviert. Sende:"
    os.system(cmd_d)
    print ""

# Button 3
def Button3(channel):
    print "Button 3 aktiviert. Sende:"
    os.system(cmd_e)
    print ""

# Button 4
def Button4(channel):
    print "Button 4 aktiviert. Sende:"
    os.system(cmd_f)
    print ""

# Button 5
def Button5(channel):
    print "Button 5 aktiviert. Sende:"
    os.system(cmd_g)
    print ""

# Button 6
def Button6(channel):
    print "Button 6 aktiviert. Sende:"
    os.system(cmd_h)
    print ""

# Interrupts
e1 = Encoder(in_a, in_b, callback = DIG1)
GPIO.add_event_detect(in_c, edge_in_c, callback = Button1, bouncetime = bouncetime)
GPIO.add_event_detect(in_d, edge_in_d, callback = Button2, bouncetime = bouncetime)
GPIO.add_event_detect(in_e, edge_in_e, callback = Button3, bouncetime = bouncetime)
GPIO.add_event_detect(in_f, edge_in_f, callback = Button4, bouncetime = bouncetime)
GPIO.add_event_detect(in_g, edge_in_g, callback = Button5, bouncetime = bouncetime)
GPIO.add_event_detect(in_h, edge_in_h, callback = Button6, bouncetime = bouncetime)

# Schleife
try:
    while True:
        time.sleep(1)

except:
  GPIO.cleanup()
  print "\nBye"
