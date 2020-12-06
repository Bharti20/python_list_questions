numbers=[50,40,23,80,56,12,5,10,700]
index=0
a=0
while index<len(numbers):
    if numbers[index] > a:
        a=numbers[index]
    index=index+1
print(a)



