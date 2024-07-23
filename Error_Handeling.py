#Exception Handeling using Try and Expect
print("Line 1")
print("Line 2")
num1=int(input("Enter The No. "))
num2=int(input("Enter the no. "))
try:
    print(num1/num2)
    print("Inside Try")
except ZeroDivisionError as e:
    print(e)
print("Line 3")
#Multiple exception handeling
print("Line 1")
print("Line 2")
num1=int(input("Enter The No. "))
num2=int(input("Enter the no. "))
try:
    print(num1/num2)
except (ZeroDivisionError,FileNotFoundError):
    print("something went wrong")
else:
    print("Else Block")
finally:
    print("Finally Block")
print("Line 3")