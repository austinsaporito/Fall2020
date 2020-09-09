#!/usr/bin/python3



def main():
    humanfile="AY707088.fasta"
    #muskitofile="test1"
    muskitofile="X79493.fasta"
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
    #column
    for i in range(2,len(humangenome)+2):
        submatrix[i][0]=humangenome[i-2]
        submatrix[i-1][1]=total
        total+=gap

    submatrix[i][1]=total
    total=0
    #row
    for i in range(2,len(muskitogenome)+2):
        submatrix[0][i]=muskitogenome[i-2]
        submatrix[1][i-1]=total
        total+=gap
    
    submatrix[1][i]=total
    for i in range(len(submatrix)):
        directionmatrix[i]=submatrix[i].copy()

    for i in range(len(submatrix)):
           for j in range(len(submatrix[i])):
               if submatrix[i][j] is None and i is not 0 and j is not 0:
                   diagnol=submatrix[i-1][j-1]
                   above=submatrix[i-1][j]
                   left=submatrix[i][j-1]
                   left+=gap
                   above+=gap
                    
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
    humanlen=len(humangenome)
    muskitolen=len(muskitogenome)

    if humanlen > muskitolen:
        traceback=muskitolen
        tracebackstring=muskitogenome
    else:
        traceback=humanlen
        tracebackstring=humangenome

    finalstring=""
    i=len(submatrix)-1
    j=len(submatrix[0])-1
    traceback-=1
    while traceback>=0:
        if directionmatrix[i][j] is "d":
            finalstring=tracebackstring[traceback]+finalstring
            i-=1
            j-=1
        elif directionmatrix[i][j] is "a" :
            finalstring="-"+finalstring
            i-=1
        elif directionmatrix[i][j] is "l":
            finalstring="-"+finalstring
            j-=1
        
        traceback-=1
    tmp=""
    tmp2=""
    for i in range(len(finalstring)):
        tmp+=finalstring[i]
        tmp2+=humangenome[i]
        if i % 25 == 0 and i is not 0:
            print(tmp)
            print(tmp2)
            print()
            tmp=""
            tmp2=""
if __name__=="__main__":
    main()