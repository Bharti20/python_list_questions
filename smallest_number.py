numbers=[8,30,4,99,2,1]
index=0
i=numbers[index]
while index<len(numbers):
    if numbers[index]<i:
       i = numbers[index]
    index=index+1
print(i)