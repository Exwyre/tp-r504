nmap -sn 172.16.0.0/24 | grep "scan report" | tr -d '()'>temp1.txt
awk '{print $NF}' temp1.txt > temp2.txt

echo "IP;TCP_OPEN;UDP_OPEN" > scan-result_2.csv
while read VAR
do
   a=$(nmap -F $VAR |grep "/tcp" | grep "open"| wc -l)
   b=$(nmap -F -sU $VAR |grep "/udp" | grep "open"| wc -l)
   echo "$VAR;$a;$b" >> scan-result_2.csv
done < temp2.txt

rm temp1.txt temp2.txt
