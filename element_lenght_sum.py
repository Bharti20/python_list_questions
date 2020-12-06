numbers=["1234","Bharti","Rubi","navgurukul"]
index=0
sum=0
sum2=0
while index<len(numbers):
    a = numbers[index]
    b=len(a)
    if b%2==0:
        sum=sum+b
    else:
        sum2=sum2+b
    index=index+1
print(sum)
print(sum2)