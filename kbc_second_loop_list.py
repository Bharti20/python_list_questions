questions_list=["How many continents are there?", "What is the capital of India?", "NG mei kaun se course padhaya jaata hai?"]   
options_list=[["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
index=0
# i=0
while index<len(questions_list):
    print(questions_list[index])
    j=0
    z=1
    while j<=len(options_list):
        print(z*1,options_list[index][j])
        j=j+1
        z=z+1
    index=index+1
    # i = i+1