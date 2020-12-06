marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
total_marks=0
index = 0
while index<len(marks):
    total_marks = total_marks+int(marks[index])
    index = index+1
print(total_marks)