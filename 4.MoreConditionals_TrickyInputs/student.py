# Name: Student Sorter
# Date:
# Author:
# Description: Write a program that determines whether the user is a senior or junior student. 
#     (Implement Years 1-12 only but make sure your program can handle weird inputs!)

# Answer:
year = input("What grade are you in? ")
if (int(year) > 10 and int(year) < 13):
    print("You are a senior student")
elif (int(year) > 0 and int(year) < 11):
    print("You are a junior student")
else:
    print("Wrong input, try again!")
