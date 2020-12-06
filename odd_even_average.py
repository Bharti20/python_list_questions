numbers=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
sum=0
sum2=0
count=0
count1=0
while index<len(numbers):
    if numbers[index]%2==0:
        count=count+1
        sum=sum+numbers[index]
    else:
        count1=count1+1
        sum2=sum2+numbers[index]
    index=index+1
print("even average",sum//count)
print("odd average",sum2//count1)