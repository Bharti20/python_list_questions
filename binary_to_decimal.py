

binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
index=0
sum=0
i =len(binary_number)-1
while index<len(binary_number):
    a = binary_number[index]*2
    b = a**i
    sum=sum+b
    i=i-1
    index=index+1
print(sum)


# binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
# decimal=0
# length=len(binary_number)-1
# c=1
# while length>=0:
#     decimal= decimal+binary_number[length]*c
#     c=c*2
#     length=length-1
# print(decimal)
    
    