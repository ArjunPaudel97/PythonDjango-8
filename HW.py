"""

First example......................

print("Main Menu........................")
print("1. Add")
print("2. Sub")
print("3. Prd")
print("4. Div")
print("5. Rem")
print("0. Exit")

result = None
choice = input("Enter your choice: ")
choice = int(choice)
if choice == 0:
    exit()

num1 = input("Enter first no: ")
num1 = int(num1)
num2 = input("Enter second number: ")
num2 = int(num2)

if choice == 1 :
    result = num1 + num2
elif choice == 2:
    result = num1 - num2
elif choice == 3:
    result = num1 * num2
elif choice == 4:
    result = num1 / num2
elif choice == 5:
    result = num1 % num2
else: 
    print("Wrong input!")

print( "Result: ", result)
"""
"""
#Second example


num1 = input("Enter a number (1-7) : ")
num1 = int(num1)
match num1:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case 6:
        print("Six")
    case 7:
        print("Seven")




#Third example


start = None
stop = input("How many times?")

value = "Broadway"
start = 1
stop = int(stop)
while start <= stop:
    print(value)
    start += 1
print("out")





a = 1
b = 10
sum = 0
while a<= b:
    print(a)
    sum = sum + a 
    a += 1

tot = sum/10

    
print("Sum:", sum)
print("Average:", tot )

"""



"""
Main Menu

1.Add
2.Display
3.Search
4.Search and Edit
5.Search and delete
0.Exit
-----------------------
ENTER YOUR CHOICE:

"""
print("Main Menu")
print("-----------------")
print("1.Add")
print("2.Display")
print("3.Search")
print("4.Search and Edit")
print("5.Search and delete")
print("0.Exit")
print("-----------------------")
ch = input("ENTER YOUR CHOICE: ")
ch = int(ch)


if ch == 1:
    add(n)




















def add(n):
    