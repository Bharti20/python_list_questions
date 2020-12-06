questions_list=["How many continents are there?", "What is the capital of India?", "NG mei kaun se course padhaya jaata hai?"]   
options_list=[["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
answer_list=["Seven", "Delhi", "Software Engineering"]
index=0
a=0
while index<len(questions_list):
    print(questions_list[index])
    j=0
    z=1
    while j<=len(options_list):
        print(z*1,options_list[index][j])
        j=j+1
        z=z+1
    user=input("enter the answer")
    if user==answer_list[a]:
        print("Congrats! Aapka answer sahi hai")
    else:
        print("Aapka jabab galat hai,isliye aapko game se bahar nikal diya gaya hai")
        break
    a=a+1
    index=index+1