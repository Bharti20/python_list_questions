numbers=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
sum=0
sum2=0
while index<len(numbers):
    if numbers[index]%2==0:
        sum=sum+numbers[index]
    else:
       sum2=sum2+numbers[index]
    index=index+1
print("even",sum)
print("odd",sum2)