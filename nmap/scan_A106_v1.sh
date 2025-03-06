#!/bin/bash

# Définition du réseau à scanner
RESEAU="172.16.0.0/24"

# Définition du fichier de sortie CSV
FICHIER_CSV="scan-result_1.csv"

# Suppression du fichier CSV s'il existe déjà
rm -f "$FICHIER_CSV"

# En-tête du fichier CSV
echo "IP,Ports_TCP_Ouverts" > "$FICHIER_CSV"

# Scan Nmap et traitement des résultats
nmap -sS "$RESEAU" -oG - | awk '/open\/tcp/ { ip=$2; ports[$ip]++; } END { for (ip in ports) { print ip "," ports[ip]; } }' >> "$FICHIER_CSV"

echo "Scan terminé. Les résultats ont été enregistrés dans $FICHIER_CSV"
