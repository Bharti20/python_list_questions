numbers=[5,6,9,-1,-1,6,3]
index=0
List=[]
while index<len(numbers):
    if numbers[index]>0:
        List.append(numbers[index])
    index=index+1
print(List)
    
    