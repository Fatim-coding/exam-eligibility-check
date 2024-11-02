#Take input for the student that he can attend the exam or not
medical_cause=input("did you have a medical cause Y or N: ")
#Take input of the attendance
attend = int(input("enter the attendance of the student: "))

#checking the user input  predicting output accordingly

if medical_cause == 'Y': #checking the condition :
    print ("you are allowed")
else:
   if attend>=75: #checking the condition 2
        print ("allowed")
   else:
    print ("not allowed")