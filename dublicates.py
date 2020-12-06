numbers=[19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
index=0
List=[]
while index<len(numbers):
    j=index+1
    while j<len(numbers):
        if numbers[index]==numbers[j] and numbers[index] not in List:
            List.append(numbers[index])
    
        j=j+1
    index=index+1
print(List)
    
   
