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
	if not t:
		return

	for i in t:
		check=Eclosurestate(i)
		temp=sorted(check)
		for j in temp:
			if j not in Tlist:
				Tlist.append(j)
	return sorted(Tlist)

def move(t,state):

	returnset=[]
	last=[]
	if not t:
		return

	for i in t:
		if not mapping[i][state]:
			continue
		else:
			for j in mapping[i][state]:
				if j not in returnset:
					returnset.append(j)
	return sorted(returnset)

def main():
#############################################
	matrix=[]
	line=sys.stdin.readline()
	for word in line.split():
		if word.isdigit():
			initialstate=int(word)

	finalstate=[]
	line=sys.stdin.readline()
	for word in line.replace("{","").replace("}","").replace(","," ").split():
		if word.isdigit():
			finalstate.append(int(word))

	line=sys.stdin.readline()
	for word in line.split():
		if word.isdigit():
			numberofstate=int(word)

	line=sys.stdin.readline()
	global states
	states=line.split()[1:]

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

###########################################
	s0=Eclosurestate(initialstate)



	stack=[]
	hadlist=[]
	stack.append(s0)
	hadlist.append(s0)
	dfamap={}
	count=1

	while stack:
		seconddfamap={}
		T=stack.pop(0)
		for i in states[:-1]:
			U=Eclosureset(move(T,i))
			if U not in hadlist:
				stack.append(U)
				hadlist.append(U)
			seconddfamap[i]=U
			dfamap[count]=seconddfamap
		count+=1

	print("before map output")
	for i in dfamap:
		print(i,dfamap[i])
		print()



if __name__=="__main__":
	main()
