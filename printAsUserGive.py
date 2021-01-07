a =["durga","bharti","sapna","sonu","bhoomi","arju"]
i=0
user=input("enter any str")
while i<len(a):
    if user in a[i][0]:
        print(a[i])
    i=i+1