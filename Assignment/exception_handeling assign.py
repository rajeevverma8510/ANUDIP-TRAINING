<<<<<<< HEAD
#Write a Python program to handle a ZeroDivisionError exception when dividing a number by,zero.
num1=int(input("Enter The No. "))
num2=int(input("Enter the no. "))
try:
    print(num1/num2)
    print("Inside Try")
except ZeroDivisionError as e:
    print(e)
#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    num=int(input("Enter a Number: "))
except ValueError as v:
    print(v)
#Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    open("anudip.txt")
except FileNotFoundError as f:
    print(f)
#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical  
try:
    num1=int(input("Enter The No. "))
    num2=int(input("Enter the no. "))
except :
=======
#Write a Python program to handle a ZeroDivisionError exception when dividing a number by,zero.
num1=int(input("Enter The No. "))
num2=int(input("Enter the no. "))
try:
    print(num1/num2)
    print("Inside Try")
except ZeroDivisionError as e:
    print(e)
#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    num=int(input("Enter a Number: "))
except ValueError as v:
    print(v)
#Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    open("anudip.txt")
except FileNotFoundError as f:
    print(f)
#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical  
try:
    num1=int(input("Enter The No. "))
    num2=int(input("Enter the no. "))
except :
>>>>>>> 08d2d173b35cf32630a2eaf6a445f4a2b4c17fb6
    print("Both Input Should be Number")