number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
index=0
List=[]
while index<len(n):
    a=index+1
    i=n[index]
    while a<len(n):
        b=n[a]
        d=i+b
        if d==number:
            c=[i,b]
            List.append(c)
           
        a = a+1
    index=index+1
print(List)