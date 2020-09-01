#!/usr/bin/python3

import math
import itertools
import re
import random

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

	randomgenome=""

	while len(randomgenome)<3:

		aval=aprob
		gval=gprob
		cval=cprob
		tval=tprob

		x=random.random()
		if x >0 and x< aval:
			randomgenome+="A"
		elif x >aval and x<gval+aval:
			randomgenome+="G"

		elif x>gval and x<cval+aval+gval:
			randomgenome+="C"
		else:
			randomgenome+="T"
		

	while len(randomgenome)<20000:
		akey=randomgenome[-3:]+"A"
		gkey=randomgenome[-3:]+"G"
		ckey=randomgenome[-3:]+"C"
		tkey=randomgenome[-3:]+"T"

		aval=genomedic[akey]
		gval=genomedic[gkey]
		cval=genomedic[ckey]
		tval=genomedic[tkey]

		x=random.random()
		if x >0 and x< aval:
			randomgenome+="A"
		elif x >aval and x<gval+aval:
			randomgenome+="G"

		elif x>gval and x<cval+aval+gval:
			randomgenome+="C"
		else:
			randomgenome+="T"

	for i in range(len(randomgenome)):
		if i %71==0:
			print()
		print(randomgenome[i],end="")


if __name__ == "__main__":
	main()
