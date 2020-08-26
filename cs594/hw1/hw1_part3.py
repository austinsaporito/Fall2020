#!/usr/bin/python3

def main():
	reversecomp=""
	f=open("lambda.fasta","r")
	trash=f.readline()
	genomestring=f.read()
	reversegenome=genomestring[::-1]

	for i in range(len(reversegenome)):
		if reversegenome[i] == "A":
			reversecomp+="T"
		elif reversegenome[i] == "T":
			reversecomp+="A"
		elif reversegenome[i] == "G":
			reversecomp+="C"
		elif reversegenome[i] == "C":
			reversecomp+="G"
		else:
			reversecomp+="\n"
	final=open("lambda.rev.fasta","a")
	final.write(">reversed")
	final.write(reversecomp)
	final.close()
	f.close()
if __name__ == "__main__":
	main()
