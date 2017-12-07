#builds hidden markov models for each protein and searches translated RNAseq files for each protein
#have to have muscle, hmmbuild, and hmmmsearch files in repo

#muscle alignment
for proteins in protein*.fasta #loops through all protein files
do 
	./muscle -in $proteins -out $proteins.align
done
#build models
for align in protein*.fasta.align #builds hmms for each protein
do
	./hmmbuild $align.hmm $align
done
#search rnaseq files for protein models
for models in protein*.fasta.align.hmm #loops through models
do
	for treatment in *.protein #loops through treatments
	do
		./hmmsearch --tblout $treatment.hits $models $treatment #creates table for each transcript, overwritten each time 
		cat $treatment.hits >> $treatment.hits.table #appends to table before previous table is overwritten
	done
done
