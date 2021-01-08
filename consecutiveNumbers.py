user=int(input("enter how many times you want to take input"))
List=[]
i=0
while i<user:
    user2=int(input("enter the number"))
    List.append(user2)
    i=i+1
list=[1,2,3,4,5]
j=1
x=0
count=0
while j<len(List):
    a=List[x]+j
    if a==List[j]:
        count=count+1
    j=j+1
if count==len(List)-1:
    print("True")
else:
    print("False")