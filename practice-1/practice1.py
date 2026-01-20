#Write a program to iput two numbers and print their sum.
a = 0
b = 0
sum = 0
print("Enter two numbers to add")
a = int(input('a ='))
b = int(input('b ='))
sum = a+b
print("The sum of ", a , " and ", b , " is: ", sum)
#END

#WAP to input side of a square and print its area
side = 0
area = 0
print("Enter the side of the square:")
side = float(input("side = "))
area = side ** 2
print("The area of the square with side ", side , " is: ", area)
#END

#WAP to input radius of a circle and print its circumference
import math
radius = 0
circumference = 0
print("Enter the radius of the circle:")
radius = float(input("radius = "))
circumference = 2 * math.pi * radius
print("The circumference of the circle with radius ", radius , " is: ", circumference)
#END       

#WAP to input temperature in Celsius and convert it to Fahrenheit
celsius = 0
fahrenheit = 0
print("Enter temperature in Celsius:")
celsius = float(input("Celsius = "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is: ", fahrenheit)
#END   

#WAP to input 2 floating point numbers abd print their average
num1 = 0.0
num2 = 0.0
average = 0.0
print("Enter two floating point numbers:")
num1 = float(input("num1 = "))
num2 = float(input("num2 = "))
average = (num1 + num2) / 2
print("The average of ", num1 , " and ", num2 , " is: ", average)
#END

#WAP to input 2 int num, a and B
#print true if a is > = b else print false
a = int(input("Enter first intiger a = "))
b = int(input("Enter second intiger b = "))
print(a >= b)  
#END