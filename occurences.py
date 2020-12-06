Char_List =["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
index=0
List2=[]
while index<len(Char_List):
    j =0
    List3=[]
    count=0
    while j<len(Char_List):
        if Char_List[index]==Char_List[j]:
            count=count+1
        j=j+1
    List3.append(Char_List[index])
    List3.append(count)
    if List3 not in List2:
        List2.append(List3)
    index=index+1
print(List2)