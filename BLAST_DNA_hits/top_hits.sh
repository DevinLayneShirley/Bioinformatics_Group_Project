#Reads all of the .csv files in the repository, takes their top line
#and moves them to a new file

for file in *.csv; do head -1 $file | cat top_hits; done


