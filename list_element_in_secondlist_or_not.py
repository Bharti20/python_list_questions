List=[1,2,3,4,5,6,8]
List2=[2,1,0,6,7]
index=0
while index<len(List):
    if List[index] not in List2:
        a=List[index]
        print(a)
    index=index+1
