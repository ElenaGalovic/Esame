#!/bin/bash

#creiamo una directory dove copiamo l'applicazione
mkdir -p dir_esame

#copiamo lo start script bash e i file Python in path opportuni
cp esecuzione.sh  dir_esame/
cp HR.py  dir_esame/
cp hist1.py  dir_esame/
cp hist2.py  dir_esame/

#attribuiamo i permessi di esecuzione corretti
chmod a+rx installazione.sh
chmod a+rx esecuzione.sh
chmod a+rx HR.py
chmod a+rx hist1.py
chmod a+rx hist2.py

#modifichiamo corretemente il PYTHONPATH e il PATH per permettere l'esecuzione dell'applicazione in un singolo comando
PYTHON_SCRIPTS_DIR="/Desktop/storage/s264413/Abilita Informatiche e telematiche/28.11.2023."
EXECUTABLE_SCRIPTS_DIR="/Desktop/storage/s264413/Abilita Informatiche e telematiche/28.11.2023."

export PYTHONPATH="$PYTHONPATH:'$PYTHON_SCRIPTS_DIR'"
export PATH="$PATH:'$EXECUTABLE_SCRIPTS_DIR'"

echo "Modified PYTHONPATH: $PYTHONPATH"
echo "Modified PATH: $PATH"

./esecuzione.sh
