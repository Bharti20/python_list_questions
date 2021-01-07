List=["a",1,2,5,"b","q"]
user =int(input())
i=len(List)
if user>len(List):
    print("invalid")
else:
    while user>0:
        i=i-1
        user=user-1
        print(List[i])