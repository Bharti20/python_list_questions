number=[2,4,6,5,1,0]
i = 0
while i<len(number):
    j = 0
    while j<len(number)-1:
        if number[j]<number[j+1] :
            number[j], number[j+1] = number[j+1], number[j]
        j += 1
    i += 1
print(number)