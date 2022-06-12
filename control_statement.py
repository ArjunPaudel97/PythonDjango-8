"""
num1 = int(input("Enter any number(0-9: )"))

if num1 == 0:
    print("Zero")
if num1 == 1:
    print("One")
if num1 == 2:
    print("Two")
if num1 == 3:
    print("Three")
if num1 == 4:
    print("Four")
if num1 == 5:
    print("Five")
if num1 == 6:
    print("Six")
if num1 == 7:
    print("Seven")
if num1 == 8:
    print("Eight")
if num1 == 9:
    print("Nine")
if num1 > 9:
    print("Greater number(0-9)")
if num1<0:
    print("Smaller number(0-9)")


#wap which accepts number
#print weekday
#declare
from unittest import result


num1 = None
#Input
num1 = int(input("Enter any number(1-7) : "))

#Process
if num1 == 1:
    result = "Sunday"
elif num1 == 2:
    result = "Monday"
elif num1 == 3:
    result = "Tuesday"
elif num1 == 4:
    result = "Wednesday"
elif num1 == 5:
    result = "Thursday"
elif num1 == 6:
    result = "Friday"
elif num1 == 7:
    result = "Saturday"
else :
    result = "Wrong input!"
#Output
print(result)


#Find largest among 3 numbers

num1 = int(input("Enter a number : "))
num2 = int(input("Enter other number : "))
num3 = int(input("Enter another number : "))

if num1 >= num2:
    if num1 >= num3 : 
        result = num1

elif num2 >= num1:
    if num2 >= num3:
        result = num2

elif num3 >= num1:
    if num3 >= num2:
        result = num3

else :
    print("Wrong input")

print("Largest numer is ", result)
"""