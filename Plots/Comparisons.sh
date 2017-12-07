#Creates table of hits for each treatment 
grep -v '#' control1.protein.hits.table_rodent | awk '{print $1,$3}' | uniq -c | awk '{print $1,$2,$3}' > Control1Counts.txt
grep -v '#' control2.protein.hits.table_rodent | awk '{print $1,$3}' | uniq -c | awk '{print $1,$2,$3}' > Control2Counts.txt
grep -v '#' obese1.protein.hits.table_rodent | awk '{print $1,$3}' | uniq -c | awk '{print $1,$2,$3}' > Obese1Counts.txt
grep -v '#' obese2.protein.hits.table_rodent | awk '{print $1,$3}' | uniq -c | awk '{print $1,$2,$3}' > Obese2Counts.txt
