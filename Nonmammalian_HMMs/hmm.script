#muscle alignment
for proteins in protein*.fasta
do 
	./muscle -in $proteins -out $proteins.align
done
#build models
for align in protein*.fasta.align
do
	./hmmbuild $align.hmm $align
done
#search rnaseq files for protein models
for models in protein*.fasta.align.hmm 
do
	for treatment in *.protein
	do
		./hmmsearch --tblout $treatment.hits $models $treatment
		cat $treatment.hits >> $treatment.hits.table
	done
done
