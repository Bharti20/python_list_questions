List=[]
i=0
while i<7:
    user=int(input("enter any number"))
    List.append(user)
    i=i+1
j=1
x=0
count=0
store=List[j+1]-List[j]
while j<len(List):
    a=List[j]-List[x]
    if a==store:
        count=count+1
    j=j+1
    x=x+1
if count==len(List)-1:
    print("True")
else:
    print("falese")
        