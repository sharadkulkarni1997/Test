#WAP to grade a student based on marks
marks=int(input('Enter the marks obtained by the student\n'))
if(marks >= 95):
    print ("Grade A+")
elif(marks >= 90):
    print ("Grade A")
elif(marks >= 80):
    print ("Grade B+")
elif(marks >= 70):
    print ("Grade B")
elif(marks >= 60):
    print ("Grade C")
elif(marks >= 50):
    print ("Grade D")
else:
    print ("Grade F")
#END

#WAP to check if a number is even or odd
num= int(input("Enter an intiger number\n"))
if(num % 2 == 0):
    print("Entered number is a even number")
else:
    print("Entered number is a odd number")
#END

#WAP to find the gratest of 3 numbers entered by the user
num1 = int(input('Enter the first number\n'))
num2 = int(input('Enter the second number\n'))
num3 = int(input('Enter the third number\n'))
if(num1 > num2):
    if(num1 > num3):
        print("The greatest of all three is the First number entered", num1)
    else:
        print("The greatest of all three is the Thirsd number entered", num3)
elif(num2 > num1):
    if(num2 > num3):
        print("The greatest of all three is the Second number entered", num2)
    else:
        print("The greatest of all three is the Third number entered", num3)
else:
    print("The greatest of all three is the Third number entered", num3)
#END

#WAP to check if a number is a multiple of 7

num4 = int(input('Please Enter a Number\n'))
if(num4 % 7 == 0):
    print('The entered number is a multiple of 7')
else:
    print('The entered number is not a multiple of 7')
#END