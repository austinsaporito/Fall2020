#!/usr/bin/python3

import random

def equation(prevtop, prevbot, chance):

	top=(prevtop *.95 * chance) 
	bottom=(prevbot * .05 * chance)

	return top,bottom

def prob(file):

	loaded6=.5
	regular=(1/6)
	loadednum=.1
	with open(file,"r") as f:
		rolls=f.read()
	rolls=rolls.replace("\n","")
	
	matrix=[None]*(len(rolls)+1)
	for i in range(len(matrix)):
		matrix[i]=[None]*2
	
	matrix[0][0]=1
	matrix[0][1]=0
	fairstr="F"
	loadedstr="F"
	fairtop=0
	loadedtop=0
	for i in range(1,len(matrix)):
		top,bottom=equation(matrix[i-1][0],matrix[i-1][1],regular)
		if top > bottom:
			fairtop=top
			matrix[i][0]=top
			fairstr+="F"
		elif bottom > top:
			fairtop=bottom
			matrix[i][0]=bottom
			fairstr+="L"

		if rolls[i-1] is "6":
			top2,bottom2=equation(matrix[i-1][1],matrix[i-1][0],loaded6)
			if top2 > bottom2:
				loadedtop=top2
				matrix[i][1]=top2
				loadedstr+="F"
			elif bottom2 > top2:
				loadedtop=bottom2
				matrix[i][1]=bottom2
				loadedstr+="L"
		else:
			top2,bottom2=equation(matrix[i-1][1],matrix[i-1][0],loadednum)
			if top2 > bottom2:
				loadedtop=top2
				matrix[i][1]=top2
				loadedstr+="F"
			elif bottom2 > top2:
				loadedtop=bottom2
				matrix[i][1]=bottom2
				loadedstr+="L"

		

	if matrix[-1][1]>matrix[-1][0]:
		print("printing loaded",loadedstr)
	else:
		print("printing fair",fairstr)
	print()

def main():

	file1="hw3_1.txt"
	file2="hw3_2.txt"
	prob(file1)
	prob(file2)

if __name__ == "__main__":
	main()
