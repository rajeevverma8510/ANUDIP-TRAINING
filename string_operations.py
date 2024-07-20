name = "I am Java Trainer"
print(name)
#slicing operations
print("name[2:4] ",name[2:4])
print("name[5:9] ",name[5:9])
print("name[:15]",name[:15])
print("name[2:]",name[2:])
print("name[:]",name[:])
print("name[0:17:3]",name[0:17:3])
print("name[::]",name[::])
print("name[::-1]",name[::-1])

#Captitalize() it convert first character of the string into uppercase.
srt ="rajeev verma"
print(srt.capitalize())
#Centre() it aling strings to centre by filling padding left and right of the string.
str = "Rajeev"
print(str.center(16,"*"))
#count() it count the no of substring in specific range
print(str.count("a"))
#find() it return the index of element of string
print(str.find("e")) 
#isalnum() it true when it find the alphanumeric in string
print(str.isalnum())
#islower() it return true if every character in string is in lower case 
print(str.islower())
#lower() it convert every charactr into lowwercase
print(str.lower())
#upper() it convert every character into uppercase
print(str.upper())
#swapcase() it convert uppercase into lowercase and vice-versa
print(str.swapcase())
#title() convert evry word first letter into uppercase
print(str.title())