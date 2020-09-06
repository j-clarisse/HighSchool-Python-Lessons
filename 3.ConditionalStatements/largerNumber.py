# Name: True/False Program
# Date:
# Author:
# Description: Write a program that takes two numbers one at a time and outputs the larger number.

# Answer: 
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))


if (num1 > num2):
    print("The larger number is the first number", num1)
elif (num2 > num1):
    print("The larger number is the second number", num2)
else:
    print("The numbers are equal", str(num1)+"=="+str(num2))