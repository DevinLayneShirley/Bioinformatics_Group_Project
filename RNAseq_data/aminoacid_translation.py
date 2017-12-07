#import necessary packages
import numpy
import pandas
import re
from sys import argv
from itertools import takewhile

#open the input files, codon files, and output files
infile1 = open("control1.fasta","r")
infile2 = open("control2.fasta","r")
infile3 = open("obese1.fasta","r")
infile4 = open("obese2.fasta","r")
codonmap = open("codonmap.txt","r")
outfile1 = open("control1_protein","w")
outfile2 = open("control2_protein","w")
outfile3 = open("obese1_protein","w")
outfile4 = open("obese2_protein","w")

#create a dictionary using the codon map
d = {}
for line in codonmap:
	(val,key) = line.split()
	d[str(key)] = val

#function that translate an input codon into the amino acid using the dictionary
def translateCodon (x):
	if x in d:
		return d[x]

#function that splits a sequence into three nucleotide codons
def splitCodons(sequence):
	result = []
	for i in range(0, len(sequence), 3):
		result.append(sequence[i:i+3])
	return result

#function that translate a nucleotide sequence to the proper amino acid sequence    
def translateSequence(sequence):
	codons = splitCodons(sequence)
	aaString = ''
	for codon in codons:
		if translateCodon(codon) == 'Stop':
			return aaString
		else:
			aaString += translateCodon(codon)
	return aaString

#regex expression to find the start codon
r1=r"([ATCG]{3,3})+?(ATG)"

#for loop for the first file
#loop through each line
for line in infile1:
	#strip the end of line character
	line = line.strip()
	#write header lines to outfile
	if line[0] == ">":
		outfile1.write(line + "\n")
	#for sequence lines
	else:
		#find the start codon and delete everything prior to it
		start = re.sub(r1,"ATG",line,count=1)
		#short = re.sub(r'.*M','M',start)
		#use functions to find the animo acid sequence
		aminoacids = translateSequence(start)
		#write the amino acid sequence to the file
		outfile1.write(aminoacids + "\n")

#same as above but for second file
for line in infile2:
	line = line.strip()
	if line[0] == ">":
		outfile2.write(line + "\n")
	else:
		start = re.sub(r1,"ATG",line,count=1)
		#short = re.sub(r'.*M','M',start)
		aminoacids = translateSequence(start)
		outfile2.write(aminoacids + "\n")

#same as 1 but for third file
for line in infile3:
	line = line.strip()
	if line[0] == ">":
		outfile3.write(line + "\n")
	else:
		start = re.sub(r1,"ATG",line,count=1)
		#short = re.sub(r'.*M','M',start)
		aminoacids = translateSequence(start)
		outfile3.write(aminoacids + "\n")

#same as 1 but for fourth file
for line in infile4:
	line = line.strip()
	if line[0] == ">":
		outfile4.write(line + "\n")
	else:
		start = re.sub(r1,"ATG",line,count=1)
		#short = re.sub(r'.*M','M',start)
		aminoacids = translateSequence(start)
		outfile4.write(aminoacids + "\n")

#close all of the files
infile1.close()
infile2.close()
infile3.close()
infile4.close()
outfile1.close()
outfile2.close()
outfile3.close()
outfile4.close()
codonmap.close()
