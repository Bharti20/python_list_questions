List=[]
i=0
while i<5:
    user=int(input("enter the number"))
    List.append(user)
    i=i+1
j=0
sum=0
sum2=0
while j<len(List):
    if List[j]%2==0:
        sum =sum+List[j]
    else:
        sum2=sum2+List[j]
    j=j+1
print(sum)
print(sum2)