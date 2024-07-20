months={"January","February","March","April","May"}
print(months)
print("Using add()---------------------------------------------")
months.add("June") #adding single data into set using add()
print("Using update()------------------------------------------")
months.update(["July","August","September"]) #adding multiple data into set using update()
print(months)
print("Using discard()-----------------------------------------")
months.discard("January") # remove the specific entered key =
print(months)
print("Using remove()-------------------------------------------")
months.remove("February") # remove the specific entered key if key not found it will throws ann error
print(months) 
print("Using pop()-----------------------------------------------")
months.pop() #remove the last elemnt of set
print(months)
print("using union()----------------------------------------------")
day1={"mon","tues","wed"}
day2={"thurs","fri","sat","sun"}
print(day1.union(day2))  #combine two sets after removing the duplicates