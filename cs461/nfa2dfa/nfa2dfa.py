#!/usr/bin/python3
import sys
def main():
	line=sys.stdin.readline()
	for word in line.split():
		if word.isdigit():
			initialstate=int(word)
	print("initial state: ",initialstate)

	finalstate=[]
	line=sys.stdin.readline()
	for word in line.replace("{","").replace("}","").replace(","," ").split():
		if word.isdigit():
			finalstate.append(int(word))
	print("final state: ",finalstate)

	line=sys.stdin.readline()
	for word in line.split():
		if word.isdigit():
			numberofstate=int(word)
	print("number of states: ",numberofstate)

	line=sys.stdin.readline()
	states=line.split()[1:]
	print("edges: ",states)

	nodes=[]
	for line in sys.stdin:
		linelist=line.split()
		nodes.append(int(linelist[0]))
		del linelist[0]
		print(linelist)

	print("nodes",nodes)

		

if __name__=="__main__":
	main()
