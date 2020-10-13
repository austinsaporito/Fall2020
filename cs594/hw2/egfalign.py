#!/usr/bin/python3



def main():
    humanfile="human_mito.fasta"
    muskitofile="neander_sample.fasta"

    with open("s","r") as hf:
        hf.readline()
        humangenome=hf.read()

    with open("t","r") as mf:
        mf.readline()
        muskitogenome=mf.read()

    humangenome=humangenome.replace("\n","")
    muskitogenome=muskitogenome.replace("\n","")


    submatrix=[None]*(len(humangenome)+2)
    directionmatrix=[None]*(len(humangenome)+2)

    for i in range(len(submatrix)):
        submatrix[i]=[None]*(len(muskitogenome)+2)
    gap=-1
    match=2
    mismatch=-1
    total=0

    submatrix[1][0]="y"
    submatrix[0][1]="y"
    #column
    for i in range(2,len(humangenome)+2):
        submatrix[i][0]=humangenome[i-2]
        submatrix[i-1][1]=total

    submatrix[i][1]=total
    total=0
    #row
    for i in range(2,len(muskitogenome)+2):
        submatrix[0][i]=muskitogenome[i-2]
        submatrix[1][i-1]=total
        
    
    submatrix[1][i]=total
    
    for i in range(len(submatrix)):
        directionmatrix[i]=submatrix[i].copy()
    biggestcolumn=0
    biggestrow=0


    for i in range(len(submatrix)):
           for j in range(len(submatrix[i])):
               if submatrix[i][j] is None and i is not 0 and j is not 0:
                   diagnol=submatrix[i-1][j-1]
                   above=submatrix[i-1][j]
                   left=submatrix[i][j-1]
                   left+=gap
                   above+=gap
                   if above < 0:
                       above=0
                   if left < 0:
                       left=0

                   if submatrix[0][j] is submatrix[i][0]:
                       diagnol+=match
                   elif submatrix[0][j] is not submatrix[i][0]:
                       diagnol+=mismatch
                   
                   if diagnol >= above and diagnol >= left:
                       submatrix[i][j]=diagnol
                       directionmatrix[i][j]="d"
                   elif above >= diagnol and above >= left:
                       submatrix[i][j]=above
                       directionmatrix[i][j]="a"
                   elif left >= above and left >= diagnol: 
                       submatrix[i][j]=left
                       directionmatrix[i][j]="l"

                   if j == len(submatrix[0])-1:
                       if submatrix[i][j] >= biggestcolumn:
                           biggestcolumn=submatrix[i][j]
                   if i == len(submatrix)-1:
                       if submatrix[i][j] >= biggestrow:
                           biggestrow=submatrix[i][j]
                    
#    for i in submatrix:
#        print(i)
#    print()
#    for i in directionmatrix:
#        print(i)
    print(biggestrow)
    print(biggestcolumn)
    if biggestrow > biggestcolumn:
        print(biggestrow)
    elif biggestcolumn > biggestrow:
        print(biggestcolumn)

if __name__=="__main__":
    main()
