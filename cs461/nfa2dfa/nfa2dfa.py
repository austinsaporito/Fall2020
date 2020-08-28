#!/usr/bin/python3

import sys

mapping={}
def Eclosurestate(state):
	stack=[]
	returnlist=[]
	hadlist=[]
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
					if i not in hadlist:
						stack.append(j)
						returnlist.append(j)
				hadlist.append(stack.pop(0))
	
	tmp = list(set(returnlist))
	tmp.sort()
	return tmp

def Eclosureset(num):
	
	Tlist=[]
	for i in range(1,num+1):
		Tlist.append(Eclosurestate(i))
	return Tlist

def move(state):
	
	returnset=[]
	for i in range(1,len(mapping)+1):
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
#	print(mapping)
#	print(Eclosurestate(4))

#	print(Eclosureset(numberofstate))

#	print(move("a"))

if __name__=="__main__":
	main()
