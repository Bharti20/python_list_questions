List=[1,2,"a",4,-4,6,7,8,9]
i=0
count=0
List2=[]
while i>=0:
    List2.append(List[i])
    count=count+1
    if List2==List:
        print(count)
        break
    i=i+1