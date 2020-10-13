#!/usr/bin/python3

import math
import itertools
import re

def main():
	L = ['A', 'C', 'G', 'T']
	genomelist=[]
	genomedic={}
	total=0
	f=open("training","r")
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

	tmp=itertools.product(L, repeat=2)
	strain=""
	for i in tmp:
		strain=""
		for x in i:
			strain+=x
		genomelist.append(strain)
	first3=""
	for i in genomelist:
		first3=""
		first3=i[0:1]
		denom=len(re.findall("(?="+first3+")",genomestring))
		num=len(re.findall("(?="+i+")",genomestring))
		if denom is not 0:
			genomedic.update({i:num/denom})
	
	print(genomedic)	
	f=open("string","r")
	trash=f.readline()
	neanderstring=f.read().replace("\n",'')
	print(neanderstring)

	lasti=0
	total=1
	for i in range(0,1):
		if neanderstring[i]=="A":
			total*=aprob
		if neanderstring[i]=="G":
			total*=gprob
		if neanderstring[i]=="C":
			total*=cprob
		if neanderstring[i]=="T":
			total*=tprob
	print(total)
	for i in range(2,len(neanderstring)+1,1):
		print(neanderstring[lasti:i])
		find=neanderstring[lasti:i]
		total*=genomedic[find]
		lasti+=1


	print("Log probability Markov:",total)


if __name__ == "__main__":
	main()
