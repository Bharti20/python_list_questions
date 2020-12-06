numbers=[23,14,56,12,90,9,15,24,25,42]
index=0
while index<len(numbers):
    if numbers[index]%2==0:
        print("it is Even","=",numbers[index])
    else:
        print("it is odd","=", numbers[index])
    index=index+1