import random #for random numbwes part1.Q3
# 1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(a,b):
    result =a/b
    print(result)
div(20,10)
# 2. Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number 
def square(a):
    result= a*a
    print(result)
square(5)
# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers.
random_numbers = [random.randint(1, 100) for _ in range(5)]
print("Random Numbers:", random_numbers)
max_number = max(random_numbers)
min_number = min(random_numbers)

print("The maximum number is:", max_number)
print("The minimum number is:", min_number)
# 4. Accept a name from the user and display that in lower case using lower() function
name = input("Enter You Name: ")
print("Name in Lower Case: ",name.lower())
#-----------------------------------------------part2-----------------------------------------------------------------------------------------------
# Write a Python program to count the occurrences of each word in a given sentence
str = "To change the overall look of your document. To change the look available in the gallery"
str.lower()
words = str.split()
word_count={}
for word in words:
    if word in word_count:
       word_count[word]+=1
    else:
       word_count[word]=1
print(word_count)
# Write a Python program to remove a newline in Python
str = "\nBest \nDeeptech \nPython \nTraining\n"    
print(str.replace("\n",""))
# Write a Python program to reverse words in a string 
str="Deeptech Python Training"
print(str[::-1])
# Write a Python program to count and display the vowels of a given text
str = "Welcome to python Training"
count = 0
lower_str=str.lower()
for i in lower_str:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count+=1
        print(i,count)
#-------------------------------------------------------------part3------------------------------------------------------------------------------------------
#Write a Python program to Count all letters, digits, and special symbols from the given string
Input = "P@#yn26at^&i5ve"
chars = 0
digit=0
symbols=0
for char in Input:
    if char.isalpha():
        chars+=1
    elif char.isdigit():
        digit+=1
    else:
        symbols+=1
print("Chars=",chars,"alpha=",digit,"symbols=",symbols)
#Write a Python program to remove duplicate characters of a given string
Input = "String and String Function"
result = []
words = Input.split()
for word in words:
    if word not in result:
         result.append(word)
print("String after removing duplicate words:", *result)
# Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
Input = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
upper=0
lower=0
special=0
num=0
for char in Input:
    if char.isupper():
        upper+=1
    elif char.islower():
        lower+=1
    elif char.isnumeric():
        num+=1
    else:
        special+=1
print("UpperCase :",upper,"LowerCase :",lower,"NumberCase :",num,"SpecialCase :",special)
#Write a Python Count vowels in a string
input= "Welcome to Python Assignment"
count = 0
lower_str=input.lower()
for i in lower_str:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count+=1
print("Total vowels are:",count)      
        