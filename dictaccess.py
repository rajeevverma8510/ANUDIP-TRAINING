#in dictionary duplication is not allowed
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print("------------------------------------------------------------------------------------")
#keys()
x = car.keys()
print(x)
print("------------------------------------------------------------------------------------")

#values()
x = car.values()
print(x)
print("------------------------------------------------------------------------------------")

#items()
x = car.items()
print(x)
print("------------------------------------------------------------------------------------")

#to find out the vales of all the elements
for x in car.values():
    print(x)
print("------------------------------------------------------------------------------------")

#get()
x=car.get("model")
print(x)

print("-------------------------------------------------------------------------------------")

