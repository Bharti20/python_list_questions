List=[[2,3,1],[2,3,4],[5,3,1]]
List2=[[1,2,3,],[3,6,7],[4,1,3]]
List4=[]
i=0
while i<len(List):
    j=0
    List3=[]
    while j<len(List):
        a=List[i][j]*List2[i][j]
        List3.append(a)
        j=j+1
    List4.append(List3)
    i = i+1
print(List4)