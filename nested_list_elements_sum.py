magic_square = [[8, 3, 4], [1, 5, 9],[6, 7, 2]]
index=0
sum=0
while index<len(magic_square):
    j=0
    while j<len(magic_square):
        a=magic_square[index][j]
        sum=sum+a
        j=j+1
    index=index+1
print(sum)