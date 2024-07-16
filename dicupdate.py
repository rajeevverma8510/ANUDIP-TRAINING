#updte the elements in Dictionary or insert multiple data on specified key value
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car.update({"year":2024})
print(car)
#adding 1 dictionary into another
print("-----------------------------------------------------------------------------------------")
car_spec = {
    "color": "white",
    "engine": "v8",
    "interior":"vegan leather"
}
car.update(car_spec)
print(car)