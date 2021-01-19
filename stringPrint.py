a=""
string=input("enter")
if len(string)==2:
    i=0
    while i<len(string):
        a=a+string
        i=i+1
    print(a)
elif len(string)==1:
    print(a)

else:
    x=0
    j=0
    while j<len(string):
        j=j+x
        if len(a)!=2:
            a=a+string[j]
        elif len(a)==3:
            continue
        else:
            a=a+string[j]
        x=x+1
    print(a)
    