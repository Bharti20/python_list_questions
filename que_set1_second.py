numbers=[50.40,23,70,56,12,5,10,7]
index =0
count=0
while index<len(numbers):
    if numbers[index]>20 and numbers[index]<40:
        print(numbers[index])
        count=count+1
    index = index+1
print(count)


