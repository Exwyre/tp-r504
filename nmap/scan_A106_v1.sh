#!/bin/bash

# Définition du réseau à scanner
nmap -sn 172.16.0.0/24 | grep "scan report" | tr -d '()'>scan_result_1.txt
awk '{print $NF}' scan_result_1.txt > scan_result_2.txt


while read VAR
do
	a=$(nmap -F $VAR | grep "/tcp" | grep "open"| wc -l)
	echo "$VAR,$a" >> scan_result_1.csv
done < scan_result_2.txt
