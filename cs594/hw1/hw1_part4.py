#!/usr/bin/python3

import re
def main():
	
	di=["AA","AC","AG","AT","CA","CC","CG","CT","GA","GC","GG","GT","TA","TC","TG","TT"]
	f=open("lambda.fasta","r")
	trash=f.readline()
	genomestring=f.read()
	genomestring=genomestring.replace("\n",'')

	acount=genomestring.count('A')
	ccount=genomestring.count('C')
	gcount=genomestring.count('G')
	tcount=genomestring.count('T')
	print("Nucleotide frequencies: ")
	print()
	print("A: ",acount/len(genomestring))
	print("C: ",ccount/len(genomestring))
	print("G: ",gcount/len(genomestring))
	print("T: ",tcount/len(genomestring))

	print()
	print("Dinucleotide frequencies:")
	print()
	for i in di:
		count=len(re.findall("(?="+i+")",genomestring))
		print(i, count/(len(genomestring)))

if __name__ == "__main__":
	main()
