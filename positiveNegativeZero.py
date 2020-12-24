List=[]
i=0
positive=0
negative=0
zero=0
while i<5:
    user=int(input("enter the number"))
    List.append(user)
    if List[i]>0:
        positive=positive+1
    elif List[i]<0:
        negative=negative+1
    else:
        zero=zero+1
    i=i+1
print("positive",positive)
print("negative",negative)
print("zero",zero)