def agecheck(age):
    if age>=18:
        print("You can Vote")
    else:
        raise ValueError("You Can't Vote")
try:
    agecheck(20)
except ValueError as e:
    print(e)