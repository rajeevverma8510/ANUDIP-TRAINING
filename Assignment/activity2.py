<<<<<<< HEAD
# creating data table using dictonary 
import pandas as pd 
from tabulate import tabulate

student_data = [
    {"stdid": 1, "stdname": "ashish kumar", "class": 10, "age": 15, "hindi": 85, "english": 78, "maths": 92, "science": 88, "computer": 90},
    {"stdid": 2, "stdname": "abhishek kumar", "class": 10, "age": 16, "hindi": 80, "english": 82, "maths": 95, "science": 91, "computer": 89},
    {"stdid": 3, "stdname": "aman", "class": 10, "age": 15, "hindi": 75, "english": 80, "maths": 88, "science": 85, "computer": 87},
    {"stdid": 4, "stdname": "rahul", "class": 10, "age": 16, "hindi": 90, "english": 88, "maths": 94, "science": 92, "computer": 93},
    {"stdid": 5, "stdname": "ruby", "class": 10, "age": 15, "hindi": 78, "english": 75, "maths": 85, "science": 80, "computer": 82},
    {"stdid": 6, "stdname": "suman", "class": 10, "age": 16, "hindi": 88, "english": 84, "maths": 89, "science": 87, "computer": 90},
    {"stdid": 7, "stdname": "saurabh", "class": 10, "age": 15, "hindi": 82, "english": 79, "maths": 90, "science": 86, "computer": 88},
    {"stdid": 8, "stdname": "sumit", "class": 10, "age": 16, "hindi": 85, "english": 83, "maths": 92, "science": 89, "computer": 91},
    {"stdid": 9, "stdname": "kamlesh", "class": 10, "age": 15, "hindi": 77, "english": 76, "maths": 84, "science": 81, "computer": 83},
    {"stdid": 10, "stdname": "rohan", "class": 10, "age": 16, "hindi": 89, "english": 85, "maths": 91, "science": 90, "computer": 92},
]
headers = ["stdid","stdname","class","age","hindi","english","maths","science","computer"]
table=[[student[header] for header in headers]for student in student_data]

# complete students detail in column form
df=pd.DataFrame(data=student_data,columns=headers)
print(df)

# to show the data in the form of table using the tabulate library of python
student_tabulate= tabulate(df,headers=headers,tablefmt="grid")
print(student_tabulate)

# student with more than 80 marks in english
for student in student_data:
    if(student['english']>80):
        a = student.values()
        print(a)
print()

# name and age of students with more marks than 40 in maths
for student in student_data:
    if(student['maths']>40):
        print(end="  "f"Name:{student['stdname']}"+"  ")
        print(f"Age:{student['age']}")
print()

# top 4 scorer in maths 

sort=sorted(student_data,key=lambda student_data : student_data['maths'],reverse=True)
print("name","age","marks")
for x in range(0,4):
    print({sort[x]["stdname"]},{sort[x]["age"]},{sort[x]['maths']})
print()

#bottom scorers in computer
sorts=sorted(student_data,key=lambda student_data : student_data['computer'])
print("name","age","marks")
z=0
for x in range(0,3):
   print({sorts[x]["stdname"]},{sorts[x]["age"]},{sorts[x]['computer']})
=======
# creating data table using dictonary 
import pandas as pd 
from tabulate import tabulate

student_data = [
    {"stdid": 1, "stdname": "ashish kumar", "class": 10, "age": 15, "hindi": 85, "english": 78, "maths": 92, "science": 88, "computer": 90},
    {"stdid": 2, "stdname": "abhishek kumar", "class": 10, "age": 16, "hindi": 80, "english": 82, "maths": 95, "science": 91, "computer": 89},
    {"stdid": 3, "stdname": "aman", "class": 10, "age": 15, "hindi": 75, "english": 80, "maths": 88, "science": 85, "computer": 87},
    {"stdid": 4, "stdname": "rahul", "class": 10, "age": 16, "hindi": 90, "english": 88, "maths": 94, "science": 92, "computer": 93},
    {"stdid": 5, "stdname": "ruby", "class": 10, "age": 15, "hindi": 78, "english": 75, "maths": 85, "science": 80, "computer": 82},
    {"stdid": 6, "stdname": "suman", "class": 10, "age": 16, "hindi": 88, "english": 84, "maths": 89, "science": 87, "computer": 90},
    {"stdid": 7, "stdname": "saurabh", "class": 10, "age": 15, "hindi": 82, "english": 79, "maths": 90, "science": 86, "computer": 88},
    {"stdid": 8, "stdname": "sumit", "class": 10, "age": 16, "hindi": 85, "english": 83, "maths": 92, "science": 89, "computer": 91},
    {"stdid": 9, "stdname": "kamlesh", "class": 10, "age": 15, "hindi": 77, "english": 76, "maths": 84, "science": 81, "computer": 83},
    {"stdid": 10, "stdname": "rohan", "class": 10, "age": 16, "hindi": 89, "english": 85, "maths": 91, "science": 90, "computer": 92},
]
headers = ["stdid","stdname","class","age","hindi","english","maths","science","computer"]
table=[[student[header] for header in headers]for student in student_data]

# complete students detail in column form
df=pd.DataFrame(data=student_data,columns=headers)
print(df)

# to show the data in the form of table using the tabulate library of python
student_tabulate= tabulate(df,headers=headers,tablefmt="grid")
print(student_tabulate)

# student with more than 80 marks in english
for student in student_data:
    if(student['english']>80):
        a = student.values()
        print(a)
print()

# name and age of students with more marks than 40 in maths
for student in student_data:
    if(student['maths']>40):
        print(end="  "f"Name:{student['stdname']}"+"  ")
        print(f"Age:{student['age']}")
print()

# top 4 scorer in maths 

sort=sorted(student_data,key=lambda student_data : student_data['maths'],reverse=True)
print("name","age","marks")
for x in range(0,4):
    print({sort[x]["stdname"]},{sort[x]["age"]},{sort[x]['maths']})
print()

#bottom scorers in computer
sorts=sorted(student_data,key=lambda student_data : student_data['computer'])
print("name","age","marks")
z=0
for x in range(0,3):
   print({sorts[x]["stdname"]},{sorts[x]["age"]},{sorts[x]['computer']})
>>>>>>> 08d2d173b35cf32630a2eaf6a445f4a2b4c17fb6
print()