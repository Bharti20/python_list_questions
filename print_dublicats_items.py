numbers=[1,2,3,1,2,2,3,4]
index=0
i= numbers[index]
list=[]
while index<len(numbers):
    if numbers[index]==i:
        a=(numbers[index])
        list.append(numbers[index])
    index=index+1
    i = i+1
print(list)
    