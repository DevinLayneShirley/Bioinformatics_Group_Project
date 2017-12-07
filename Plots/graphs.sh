#Creates table of hits for each treatment 
#searches for unique hits and adds them up
grep -v '#' control1.protein.hits.table_rodent | awk '{print $1,$3}' | uniq -c | awk '{print $1,$2,$3}' > Control1Counts.txt
grep -v '#' control2.protein.hits.table_rodent | awk '{print $1,$3}' | uniq -c | awk '{print $1,$2,$3}' > Control2Counts.txt
grep -v '#' obese1.protein.hits.table_rodent | awk '{print $1,$3}' | uniq -c | awk '{print $1,$2,$3}' > Obese1Counts.txt
grep -v '#' obese2.protein.hits.table_rodent | awk '{print $1,$3}' | uniq -c | awk '{print $1,$2,$3}' > Obese2Counts.txt


#replaces the proteins with the short hand from the paper
for files in *.txt
do
	sed -i 's/protein1.fasta/Gsta2/g' $files 
	sed -i 's/protein2.fasta/Slc7a12/g' $files
	sed -i 's/protein3.fasta/Tpra1/g' $files
	sed -i 's/protein4.fasta/Ptpn5/g' $files
	sed -i 's/protein5.fasta/Lhx2/g' $files
	sed -i 's/protein6.fasta/Synpr/g' $files
done

cat *.txt > expressionlevels.txt
