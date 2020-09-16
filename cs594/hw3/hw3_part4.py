#!/usr/bin/python3

import random

def equation(prevtop, prevbot, chance):

	return (prevtop *.95 * chance) + (prevbot * .05 * chance)

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
	for i in range(1,len(matrix)):
		matrix[i][0]=equation(matrix[i-1][0],matrix[i-1][1],regular)

		if rolls[i-1] is "6":
			matrix[i][1]=equation(matrix[i-1][1],matrix[i-1][0],loaded6)
		else:
			matrix[i][1]=equation(matrix[i-1][1],matrix[i-1][0],loadednum)

	print(matrix[-1][1]+matrix[-1][0])

def main():

	file1="hw3_1.txt"
	file2="hw3_2.txt"
	prob(file1)
	prob(file2)

if __name__ == "__main__":
	main()
