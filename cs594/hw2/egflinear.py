#!/usr/bin/python3



def main():
    humanfile="human_mito.fasta"
    #muskitofile="test1"
    muskitofile="neander_sample.fasta"
    #humanfile="test2"

    with open(humanfile,"r") as hf:
        hf.readline()
        humangenome=hf.read()

    with open(muskitofile,"r") as mf:
        mf.readline()
        muskitogenome=mf.read()

    humangenome=humangenome.replace("\n","")
    muskitogenome=muskitogenome.replace("\n","")

    #humangenome=humangenome[:5]
    #muskitogenome=muskitogenome[:5]

    submatrix=[None]*(len(humangenome)+2)
    directionmatrix=[None]*(len(humangenome)+2)

    for i in range(len(submatrix)):
        submatrix[i]=[None]*(len(muskitogenome)+2)
    gap=-2
    match=2
    mismatch=-1
    total=0

    submatrix[1][0]="y"
    submatrix[0][1]="y"
    maxcolumn=len(humangenome)+2
    #column
    for i in range(2,len(humangenome)+2):
        submatrix[i][0]=humangenome[i-2]
        submatrix[i-1][1]=total

    submatrix[i][1]=total
    total=0
    maxrow=len(muskitogenome)+2
    #row
    for i in range(2,len(muskitogenome)+2):
        submatrix[0][i]=muskitogenome[i-2]
        submatrix[1][i-1]=total
        
    
    submatrix[1][i]=total
    #for i in submatrix:
    #    print(i)
    #exit()
    
    for i in range(len(submatrix)):
        directionmatrix[i]=submatrix[i].copy()
    highesti=0
    highestj=0
    highest=0
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
                       if diagnol > highest:
                           highest=diagnol
                           highesti=i
                           highestj=j
                   elif above >= diagnol and above >= left:
                       submatrix[i][j]=above
                       directionmatrix[i][j]="a"
                       if above > highest:
                           highest=diagnol
                           highesti=i
                           highestj=j
                   elif left >= above and left >= diagnol: 
                       submatrix[i][j]=left
                       directionmatrix[i][j]="l"
                       if left > highest:
                           highest=diagnol
                           highesti=i
                           highestj=j

                   if j == len(submatrix[0])-1:
                       if submatrix[i][j] >= biggestcolumn:
                           biggestcolumn=submatrix[i][j]
                   if i == len(submatrix)-1:
                       if submatrix[i][j] >= biggestrow:
                           biggestrow=submatrix[i][j]
                    
    humanlen=len(humangenome)
    muskitolen=len(muskitogenome)
    if biggestrow > biggestcolumn:
        print(biggestrow)
    elif biggestcolumn > biggestrow:
        print(biggestcolumn)

if __name__=="__main__":
    main()