month=["jan","feb","march","april","may","june","july","Aug","Sept","oct","nov","dec"]
user=int(input("enter the number"))
if user<=0 or user>=13:
    print("invalid")
else:
    a=user-1
    value=month[a]
    print(value)