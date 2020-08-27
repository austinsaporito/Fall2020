#!/usr/bin/python3
import sys
def main():
	matrix=[]
	mapping={}
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
	
	for i in mapping:
		print(i,mapping[i])


if __name__=="__main__":
	main()
