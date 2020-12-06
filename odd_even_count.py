numbers=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
count=0
count1=0
while index<len(numbers):
    if numbers[index]%2==0:
        count=count+1
    else:
        count1=count1+1
    index=index+1
print("even",count)
print("odd",count1)