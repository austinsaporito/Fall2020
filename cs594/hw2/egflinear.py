#!/usr/bin/python3



def main():
    humanfile="human_mito.fasta"
    muskitofile="neander_sample.fasta"

    with open(humanfile,"r") as hf:
        hf.readline()
        humangenome=hf.read()

    with open(muskitofile,"r") as mf:
        mf.readline()
        muskitogenome=mf.read()

    humangenome=humangenome.replace("\n","")
    muskitogenome=muskitogenome.replace("\n","")


    columnmatrix=[None]*(len(humangenome)+2)

    rowmatrix=[None]*(len(muskitogenome)+2)
    gap=-2
    match=2
    mismatch=-1

    columnmatrix[1]="y"
    rowmatrix[1]="y"
    #column
    for i in range(2,len(humangenome)+2):
        columnmatrix[i]=humangenome[i-2]

    #row
    for i in range(2,len(muskitogenome)+2):
        rowmatrix[i]=muskitogenome[i-2]

    outermatrix=[None]*2
    for i in range(2):
        outermatrix[i]=[0]*(len(rowmatrix)-1)
    
    biggestrow=0
    biggestcolumn=0
    for i in range(1,len(columnmatrix)):
        for j in range(1,len(rowmatrix)):
            diagnol=outermatrix[0][j-2]
            above=outermatrix[0][j-1]
            left=outermatrix[1][j-2]
            left+=gap
            above+=gap
            if above < 0:
                above=0
            if left < 0:
                left=0

            if rowmatrix[j] is columnmatrix[i]:
                diagnol+=match
            elif rowmatrix[j] is not columnmatrix[i]:
                diagnol+=mismatch
            if j-1 != 0:
                if diagnol >= above and diagnol >= left:
                    outermatrix[1][j-1]=diagnol
                elif above >= diagnol and above >= left:
                    outermatrix[1][j-1]=above
                elif left >= above and left >= diagnol: 
                    outermatrix[1][j-1]=left

            if j == len(rowmatrix)-1:
                if outermatrix[1][j-1] >= biggestcolumn:
                    biggestcolumn=outermatrix[1][j-1]
            if i == len(columnmatrix)-1:
                if outermatrix[1][j-1] >= biggestrow:
                    biggestrow=outermatrix[1][j-1]
        outermatrix[0]=outermatrix[1].copy()
        for k in range(len(outermatrix[0])):
            outermatrix[1][k]=0


    if biggestrow > biggestcolumn:
        print(biggestrow)
    elif biggestcolumn > biggestrow:
        print(biggestcolumn)

if __name__=="__main__":
    main()
