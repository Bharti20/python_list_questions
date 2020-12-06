magic_square = [[8, 3, 4], [1, 5, 9],[6, 7, 2]]
index=0
while index<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square):
        a=magic_square[index][j]
        sum=sum+a
        j=j+1
   index=index+1

# for colon

List = [[8, 3, 4], [1, 5, 9],[6, 7, 2]]
i=0
while i<len(List):
    j=0
    sum=0
    while j<len(List):
        a=(List[j] [i])
        sum=sum+a
        j=j+1
    i = i+1
print(sum)

#Left Diognole

List = [[8, 3, 4], [1, 5, 9],[6, 7, 2]]
i=0
while i<len(List):
    j=0
    sum=0
    while j<len(List):
        a=(List[j] [i])
        sum=sum+a
        j=j+1
        i=i+1
    i = i+1
print(sum)

#Right Diogole 
List = [[8, 3, 4], [1, 5, 9],[6, 7, 2]]
i=2
while i>0:
    j=0
    sum=0
    while j<len(List):
        a=(List[j] [i])
        sum=sum+a
        j=j+1
        i=i-1
    i = i-i
print(sum)


magic_square = [[8, 3, 4], [1, 5, 9],[6, 7, 2]]
index=0
sum=0
sum2=0
sum3=0
sum4=0
while index<len(magic_square):
    j=0
    while j<len(magic_square):
        a=magic_square[index][j]
        sum=sum+a
        b=(magic_square[j] [index])
        sum2=sum2+b
        c=(magic_square[j] [index])
        sum3=sum3+c
        d=(magic_square [j] [index])
        sum4=sum4+d
        j=j+1
    index=index+1
if sum==sum2==sum3==sum4:
    print("magic square hai")
else:
    print("not")