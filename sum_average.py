marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i =0
while i<len(marks):
    a=0
    sum=0
    while a<len(marks[i]):
        d=marks[i][a]
        sum=sum+d
        a = a+1
    print(sum//a)
    i = i+1

     