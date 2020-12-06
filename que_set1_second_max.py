numbers=[0,4,230,8,50,120,5,10,7]
index=0
first_max=0
second_max=0
while index<len(numbers):
    if numbers[index] > first_max:
        first_max=numbers[index]
    index=index+1
index=0
while index<len(numbers):
    if numbers[index]>second_max and numbers[index]<first_max:
        second_max=numbers[index]
    index=index+1
    
print("first max","=",first_max)
print("second max","=",second_max)