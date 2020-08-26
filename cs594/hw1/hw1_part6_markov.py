#!/usr/bin/python3

import math
import itertools
import re

def main():
	L = ['A', 'C', 'G', 'T']
	genomelist=[]
	genomedic={}
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

	tmp=itertools.product(L, repeat=4)
	strain=""
	for i in tmp:
		strain=""
		for x in i:
			strain+=x
		genomelist.append(strain)
	first3=""
	for i in genomelist:
		first3=""
		first3=i[0:3]
		denom=len(re.findall("(?="+first3+")",genomestring))
		num=len(re.findall("(?="+i+")",genomestring))
		genomedic.update({i:num/denom})
	
	
	f=open("neander_sample.fasta","r")
	trash=f.readline()
	neanderstring=f.read().replace("\n",'')

	lasti=0
	total=0
	for i in range(0,4):
		if neanderstring[i]=="A":
			total+=math.log(aprob)
		if neanderstring[i]=="G":
			total+=math.log(gprob)
		if neanderstring[i]=="C":
			total+=math.log(cprob)
		if neanderstring[i]=="T":
			total+=math.log(tprob)

	for i in range(4,len(neanderstring),1):
		find=neanderstring[lasti:i]
		total+=math.log(genomedic[find])
		lasti+=1

	print(total)


if __name__ == "__main__":
	main()
