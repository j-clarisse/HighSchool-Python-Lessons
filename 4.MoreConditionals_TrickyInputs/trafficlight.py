# Name: Traffic Lights Program
# Date:
# Author:
# Description: Strings can also be compared using comparison operators. Write a program that imitates a stop light.

# Answer: 
light = input("Choose colour (green, yellow, red): ")

if (light == "green"):
    print("GO")
elif (light == "yellow"):
    print("SLOW DOWN")
elif (light == "red"):
    print("STOP")
else:
    print("Wrong input, try again!")
