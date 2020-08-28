#!/usr/bin/python3

import sys
import random

mapping={}
def Eclosurestate(state):

	stack=[]
	returnlist=[]
	returnlist.append(state)
	for i in mapping[state]["E"]:
		stack.append(i)
		returnlist.append(i)

	while stack:
		for i in stack:
			if mapping[i]["E"]=="{}":
				continue
			else:
				for j in mapping[i]["E"]:
					if j not in returnlist:
						stack.append(j)
						returnlist.append(j)
		stack.pop(0)
	return sorted(returnlist)

def Eclosureset(t):
	
	Tlist=[]
	for i in t:
		for j in i:
			Tlist.append(Eclosurestate(j))
	return Tlist

def move(t,state):
	returnset=[]

	for i in t:
		if not mapping[i][state]:
			continue
		else:
			returnset.append(mapping[i][state])
	return returnset

def main():
	matrix=[]
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

	for line in sys.stdin:
		linelist=line.replace("{}","-").replace("{","").replace("}","").split()
		state=int(linelist[0])
		del linelist[0]
		mapping[state]={}
		seconddic={}
		for i in states:	
			seconddic[i]={}
		count=0
		for i in linelist:
			if i =="-":
				count+=1
				continue
			else:
				i=i.replace(","," ").split()
				for j in range(len(i)):
					i[j]=int(i[j])
				seconddic[states[count]]=i
				count+=1
		mapping[state]=seconddic

	s0=Eclosurestate(initialstate)

	stack=[]
	stack.append(s0)

	hadlist=[]
	while stack:
	#	print("stack",stack)
		T=stack[0]
		stack.pop(0)
		for i in states[:-1]:
		#	print("set to look at",T)
		#	print("edge: ",i)
			U=Eclosureset(move(T,i))
		#	print("U: ",U)
			for k in U:
		#		print("U",k)
				if k not in hadlist:
					stack.append(k)
					hadlist.append(k)
	for i in hadlist:
		print(i)


	





	

if __name__=="__main__":
	main()
