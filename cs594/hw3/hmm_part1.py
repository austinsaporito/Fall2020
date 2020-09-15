#!/usr/bin/python3

import random

def equation(prev, chance, transition):

	if transition == "loaded":
		return (prev *.95 * chance) + (prev * .05 * chance)
	elif transition == "fair":
		return (prev *.95 * chance) + (prev * .05 * chance)

def main():
	
	diceroll=[]
	swap="fair"
	traceback=""
	flag=0
	for i in range(300):
		switch=random.randint(0,100)
		number=random.random()	
		if switch <=5 and flag==1:
			if swap=="loaded":
				swap="fair"
			elif swap == "fair":
				swap="loaded"
			
		flag=1
		if swap == "loaded":
			traceback+="l"
			if number <= 1 and number >.5:
				diceroll.append(6)
			if number <= 5/10 and number >4/10:
				diceroll.append(5)
			elif number <= 4/10 and number >3/10:
				diceroll.append(4)
			elif number <= 3/10 and number >2/10:
				diceroll.append(3)
			elif number <= 2/10 and number >1/10:
				diceroll.append(2)
			elif number <= 1/10 and number >=0:
				diceroll.append(1)
		elif swap == "fair":
			traceback+="f"
			if number <= 1 and number >(5/6):
				diceroll.append(6)
			if number <= (5/6) and number >(4/6):
				diceroll.append(5)
			elif number <= 4/6 and number >3/6:
				diceroll.append(4)
			elif number <= 3/6 and number >2/6:
				diceroll.append(3)
			elif number <= 2/6 and number >1/6:
				diceroll.append(2)
			elif number <= 1/6 and number >=0:
				diceroll.append(1)

		
	print(diceroll)
	print(traceback)



if __name__ == "__main__":
	main()
