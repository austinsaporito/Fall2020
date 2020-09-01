#!/usr/bin/python3

import math

def main():
	total=0
	f=open("human_mito.fasta","r")
	trash=f.readline()
	genomestring=f.read()
	genomestring=genomestring.replace("\n",'')
	genomelength=len(genomestring)
	f.close()

	acount=genomestring.count('A')
	ccount=genomestring.count('C')
	gcount=genomestring.count('G')
	tcount=genomestring.count('T')

	aprob=acount/genomelength
	cprob=ccount/genomelength
	gprob=gcount/genomelength
	tprob=tcount/genomelength
	
	f=open("neander_sample.fasta","r")
	trash=f.readline()
	neanderstring=f.read()
	neanderstring=neanderstring.replace("\n","")

	for i in neanderstring:
		if i =="A":
			total+=math.log(aprob)	
		if i =="C":
			total+=math.log(cprob)	
		if i =="G":
			total+=math.log(gprob)	
		if i =="T":
			total+=math.log(tprob)	

	print("Log probabilty multinomial: ",total)


if __name__ == "__main__":
	main()
