List=[2,4,5,6,7,3,1]
k=3
i=0
List2=[]
while i<len(List)-2:
    j=i
    sum=0
    while j<k:
        sum = sum+List[j]
        j=j+1
    List2.append(sum)
    i=i+1
    k=k+1
print(List2)
