#!/usr/bin/python3



def main():
    humanfile="AY707088.fasta"
    muskitofile="X79493.fasta"

    with open(humanfile,"r") as hf:
        hf.readline()
        humangenome=hf.read()

    with open(muskitofile,"r") as mf:
        mf.readline()
        muskitogenome=mf.read()

    humangenome=humangenome.replace("\n","")
    print(len(humangenome))
    muskitogenome=muskitogenome.replace("\n","")

    humangenome=humangenome[:5]
    muskitogenome=muskitogenome[:5]

    submatrix=[None]*(len(humangenome)+2)

    for i in range(len(submatrix)):
        submatrix[i]=[None]*(len(muskitogenome)+2)

    gap=-2
    match=2
    mismatch=-1
    total=0

    submatrix[1][0]="lamda"
    submatrix[0][1]="lamda"
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
           for j in range(len(submatrix[i])):
               if submatrix[i][j] is None and i is not 0 and j is not 0:
                   diagnol=submatrix[i-1][j-1]
                   above=submatrix[i-1][j]
                   left=submatrix[i][j-1]+gap

                   if submatrix[0][j] is submatrix[i][0]:
                       diagnol+=match
                   else:
                       diagnol+=mismatch

                   if diagnol > above and diagnol > left:
                       submatrix[i][j]=diagnol
                   elif above > diagnol and above > left:
                       submatrix[i][j]=above
                   else: 
                       submatrix[i][j]=left

    for i in submatrix:
        print(i)




if __name__=="__main__":
    main()