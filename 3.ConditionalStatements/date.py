# Name: Dates (Concatenation Recap)
# Date:
# Author:
# Description: Write a program that asks the user for the time, day, date, month and year. 
#     Store these into variables and then print the complete time and date as shown: 
#     “It is [TIME] on [DAY], [DATE] [MONTH], [YEAR]”.



# Answer:
time = input("What is the time? ")
day = input("What is the day? ")
date = input("What is the date (DD)? ")
month = input("What is the monty (MM)? ")
year = input("What is the year (YYYY)? ")

print("It is", time, "on", day+",", date+"/"+month+"/"+year)
