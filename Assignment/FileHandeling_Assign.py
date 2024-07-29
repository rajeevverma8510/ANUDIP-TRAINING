import pickle
#Write a program to count the occurence of word "INDIA" in a text file India.txt
file=open("India.txt",'w')
file.write("INDIA INDIA INDIA INDIA ")
file=open("India.txt",'r')
c=file.read()
word=c.split()
count=0
for i in word:
    if i=='INDIA':
       count+=1
print(count) 
file.close()

#Write a Program to count and display thelines starting with "T" in a text file story.txt
file=open("story.txt",'w')
file.write("The quick brown fox jumps over the lazy dog. \n")
file.write("INDIA is a diverse country with rich cultural heritage.\n")
file.write("Technology is advancing at an unprecedented pace.\n")
file.write("Hello, welcome to the python class.\n")
file.write("Tomorrow, we will explore more advanced topics.\n")
file.write("Taking small steps every day leads to big achievements.\n")
file.close()
file=open("story.txt",'r')
counts=0
content=file.readlines()
for i in content:
    if i[0] == 'T':
        print(i,end="")
        counts+=1
print(counts)
file.close()
#Write a program to count the number of vowels and consonants in a file "Myfile.txt"
file=open("Myfile.txt",'w')
file.write("The quick brown fox jumps over the lazy dog. \n")
file.close()
file=open("Myfile.txt",'r')
v=file.read()
vowels="aeiouAEIOU"
vow=0
con=0
for i in v:
    if i in vowels:
        vow+=1
    elif i.isalpha() and i not in vowels :
        con+=1
print("Vowels=",vow,"Consonants=",con)
file.close()
#Write a program to count and display number of words starting with "I" in a file "Word.txt"
file=open("Word.txt",'w')
file.write("The Ice Cream Independance. \n")
file.close()
file=open("Word.txt",'r')
I=file.read()
count=0
for i in I:
    if i=="i" or i=="I":
        count+=1
print(count)
#Write a program to display the lines having more than five words in a text file "Notes.txt"
file=open("Notes.txt",'w')
file.write("The Ice Cream Independance Every Child Dream . \n")
file.close()
file=open("Notes.txt",'r')
F=file.read()
word=F.split()
count=0
five=0
for i in word:
    if len(i)==5:
        five+=1
print("five words in a text file",five)
# WAP to create a binary file "stu.dat" and enter students roll number name and marks till user wants
file=open("Stu.dat","wb")

while True:
    roll_number = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
                
    student = {
        'roll_number': roll_number,
        'name': name,
        'marks': marks
        }
            
            # Serialize the student dictionary and write it to the binary file
    pickle.dump(student, file)
            
    more = input("Do you want to enter another record? (y/n): ").strip().lower()
    if more != 'yes':
        break
file.close()


#write a program to read a binary file storage display the record of student having marks greater than 81
fil=open("Stu.dat","rb")
while True:
    student = pickle.load(fil)
    if student['marks'] > 81:
        print(f"Roll Number: {student['roll_number']}, Name: {student['name']}, Marks: {student['marks']}")
        break
       
fil.close()
        
