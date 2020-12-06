numbers=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
sum=0
sum2=0
count=0
count1=1
count2=0
sum=0
sum1=0
sum2=0
while index<len(numbers):
    sum2=sum2+numbers[index]
    count=count+1
    if numbers[index]%2==0:
        sum=sum+1
        count1=count1+1
        sum=sum+numbers[index]
    else:
        sum1=sum1+1
        count2=count2+1
        # sum2=sum2+numbers[index]
    index=index+1
print("even number","=",count1)
print("odd number","=",count2)
print("saare number","=",count)
print("even sum ka sum","=",sum)
print("odd sum ka sum","=",sum1)
print("saare number ka sum","=",sum2)
print("even average","=",sum//count)
print("odd average","=",sum2//count1)
print("saare number ka average","=", sum2//count)