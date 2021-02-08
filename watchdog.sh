#!/bin/bash

pgrep -f radiotasten.py >/dev/null 2>&1
if [[ $? -eq 1 ]]
then
  echo "Skript wird neu gestartet"
  ./radiotasten.py &
else
  echo "Skript läuft noch"
fi

