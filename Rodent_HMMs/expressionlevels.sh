#lists the number of hits for a protein for each treatment, the output of this can be copied into excel to generate a table 
for file in *.table_rodent
	do
	cat $file | grep -v '#' | grep -c 'protein1'
	cat $file | grep -v '#' | grep -c 'protein2'
	cat $file | grep -v '#' | grep -c 'protein3'
	cat $file | grep -v '#' | grep -c 'protein4'
	cat $file | grep -v '#' | grep -c 'protein5'
	cat $file | grep -v '#' | grep -c 'protein6'
	done
