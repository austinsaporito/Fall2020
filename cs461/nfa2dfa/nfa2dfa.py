#!/usr/bin/python3

'''
Austin Saporito
PA1
NFA2DFA:
	Takes an NFA in stdin and converts it to a DFA on std out

'''

import sys
import random

mapping={}
'''
Pretty much ripped from the book. It takes the NFA state 'state' and return all the states 
it can go to from E transitions alone
'''
def Eclosurestate(state):

	stack=[]
	returnlist=[]
	returnlist.append(state)
	'''
	Initializing the stacklist with the given state
	'''
	for i in mapping[state]["E"]:
		stack.append(i)
		returnlist.append(i)
	'''
	exactly what it looks like adds anything that the state on the stack can go to with E 
	transitions alone ignoring if it has nothing and returning that list
	'''
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

'''
I also got this function from the book. you give it a set of states and checks it that state can reach any other state on 
E transitions using the above function and adds them on the list if not already in it to avoid duplicates
'''
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

'''
Second to last thing I got from the book lol. This function takes a set and a state and returns a list of everynode that can be reached from the given transition state
'''
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
	'''
	Super boring stuff of just reading the input nothing really to explain here
	'''


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

	'''
	We do this once on the initial state to populate our stack
	'''
	s0=Eclosurestate(initialstate)

	stack=[]
	hadlist=[]
	stack.append(s0)
	hadlist.append(s0)
	dfamap={}
	nodemapping=[]	
	count=1

	nodemapping.append(s0)
	'''
	Last time I got something from the book. Using all the functions to actually make the DFA  
	'''
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
	'''
	Everything below is to mape the set of nodes to one new node to use late and then 
	a bunch of printing out and formatting stuff, also boring
	'''
	hadlist=[]
	for i in dfamap:
		for k in states[:-1]:
			if dfamap[i][k] != None and dfamap[i][k] not in hadlist:
				nodemapping.append(dfamap[i][k])
				hadlist.append(dfamap[i][k])
				count+=1

	print("reading NFA ... done.\n\ncreating corresponding DFA ...")
	for i in range(len(nodemapping)):
		print("New DFA state:\t",i+1,"-->\t", nodemapping[i])  
	print("done.\n")

	print("Final DFA:")
	print("Initial state: 1")
	newfinal=[]
	for i in range(len(nodemapping)):
		for j in finalstate:
			if j in nodemapping[i] and (i+1) not in newfinal:
				newfinal.append(i+1)
	
	print("Final States: ", newfinal)
	print("Total States: ",len(nodemapping))
	
	print("State\t ",end="")
	for i in states[:-1]:
		print(i,"\t\t",end="")
	print()
	count=1
	for i in dfamap:
		print(count,end="\t")
		for j in states[:-1]:
			if dfamap[i][j] in nodemapping:
				node=nodemapping.index(dfamap[i][j])
				print("{",node+1,"}",end="\t\t")
			if dfamap[i][j] is None:
				print("{}",end="\t\t")
		print()
		count+=1
if __name__=="__main__":
	main()
