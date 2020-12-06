List=[[4,5],[1,2,3],[4,5],[8,9],[10,11]]
index=0
i=0
while index<len(List):
    j=index+1
    while j<len(List):
        if List[index]==List[j]:
            List.remove(List[index])
        j=j+1
    index=index+1
print(List)