#!/usr/bin/python3

import random
def equation(prevtop, prevbot, chance,probtop,probbot):

	top=(prevtop * probtop * chance) 
	bottom=(prevbot * probbot * chance)

	return top,bottom

def prob(file):

	loaded6=1
	regular=(.5)
	loadednum=0
#	with open(file,"r") as f:
#		rolls=f.read()
#	rolls=rolls.replace("\n","")
	rolls="HTT"
	
	matrix=[None]*(len(rolls)+1)
	for i in range(len(matrix)):
		matrix[i]=[None]*2
	
	matrix[0][0]=.5
	matrix[0][1]=.5
	print(matrix)
	fairstr=""
	loadedstr=""
	fairtop=0
	loadedtop=0

	selffair=.8
	selfswap=.2
	loadedswap=.2
	selfloaded=.8

	for i in range(1, len(matrix)):
		top,bottom=equation(matrix[i-1][0],matrix[i-1][1],regular,selffair,loadedswap)
		if top > bottom:
			fairtop=top
			matrix[i][0]=top
			fairstr+="F"
		elif bottom > top:
			fairtop=bottom
			matrix[i][0]=bottom
			fairstr+="L"
		
		if rolls[i-1] is "T":
			top2,bottom2=equation(matrix[i-1][1],matrix[i-1][0],loaded6,selfloaded,selfswap)
			if top2 > bottom2:
				loadedtop=top2
				matrix[i][1]=top2
				loadedstr+="L"
			elif bottom2 > top2:
				loadedtop=bottom2
				matrix[i][1]=bottom2
				loadedstr+="F"
		else:
			top2,bottom2=equation(matrix[i-1][1],matrix[i-1][0],loadednum,selfloaded,selfswap)
			if top2 > bottom2:
				loadedtop=top2
				matrix[i][1]=top2
				loadedstr+="L"
			elif bottom2 > top2:
				loadedtop=bottom2
				matrix[i][1]=bottom2
				loadedstr+="F"
		

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
