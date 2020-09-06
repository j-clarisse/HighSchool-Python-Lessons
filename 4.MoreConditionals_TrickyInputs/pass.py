# Name: Traffic Lights Program
# Date:
# Author:
# Description: Program takes in student's mark and prints whether they passed or not.

# Answer:
mark = input("What is your mark? ")
if (int(mark) >= 50):
    print("Congrats, you passed!")
elif (int(mark) >= 0):
    print("You failed :(")
else:
    print("INVALID MARK")