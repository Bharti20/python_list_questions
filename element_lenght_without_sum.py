numbers=["1234","Bharti","Rubi","navgurukul"]
index=0
sum=0
sum2=0
while index<len(numbers):
    j=0
    count=0
    while j<len(numbers[index]):
        a= numbers[index][j]
        count=count+1
        j=j+1
    if count%2==0:
        sum=sum+count
    else:
        sum2=sum2+count
    index=index+1
print("even",sum)
print("odd",sum2)