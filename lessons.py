# a program to calculate the average of 5 courses for multipuly students

# remark
def remark(studentScore,studentName):
    if(studentScore >= 70):
        if(studentScore > 100):
            studentScore=100
            print("\nName: ",studentName,"\nTotal Score: ",studentScore,"\nGrade: A")
    elif(studentScore >= 60 <69):
        print("Name: ",studentName,"\nTotal Score: ",studentScore,"\nGrade: B")
    elif(studentScore >= 50 <59):
        print("Name: ",studentName,"\nTotal Score: ",studentScore,"\nGrade: C")
    elif(studentScore >= 45 <49):
        print("Name: ",studentName,"\nTotal Score: ",studentScore,"\nGrade: D")
    elif(studentScore >= 40 <44):
        print("Name: ",studentName,"\nTotal Score: ",studentScore,"\nGrade: E")
    elif(studentScore <40):
        print("Name: ",studentName,"\nTotal Score: ",studentScore,"\nGrade: ")
    else:
       print("Name: ",studentName,"\nTotal Score: ",studentScore,"\nGrade: Missing Sricpt")
    
# average calculation
def userComputation(a,b,c,d,e,studentName):
    abcde = (a + b + c + d + e) /5

    remark(abcde,studentName)

# student data
def userInput():
    studentName= str(input("Enter Your Name => "))
    english = float(input("Please enter English Marks =>  "))
    math = float(input("Please enter Math score: "))
    computers = float(input("Please enter Computer Marks =>  "))
    physics = float(input("Please enter Physics Marks =>  "))
    chemistry = float(input("Please enter Chemistry Marks =>  "))

    userComputation(english , math , computers , physics , chemistry, studentName)


userInput()