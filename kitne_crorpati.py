kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
count1=0
count2=0
count=0
index=0
while index<len(kitna_paisa_hai):
    if kitna_paisa_hai[index]>=10000000:
        count=count+1
    elif kitna_paisa_hai[index]>=100000:
        count1=count1+1
    else:
        count2=count2+1
    index=index+1
print("Crorepati hai","=",count)
print("Lakhpati hai","=",count1)
print("Dilwale hai","=",count2)