import numpy as np
#creation of arrays
a=np.array(42)
b=np.array([1,2,2,3,4])
c= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
d=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("a array",a)
print("b array",b)
print("c array",c)
print("d array",d)
#using .ndim to get the dimensions of array 
print("a array dime",a.ndim)
print("b array dime",b.ndim)
print("c array dime",c.ndim)
print("d array dime",d.ndim)

#slicing
arr=np.array([1,2,3,4,5,6,7,8])
sarr = arr[1:5]
print(arr)
print(sarr)
sarr[2]=100   # Changing value in copy array will also be reflected in origial Array i.e it is just a view of original array.
print(arr)
print(sarr)
#copy function,The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
arr=np.array([1,2,3,4,5])
arr2=arr.copy()
arr[0]=42
print(arr)
print(arr2)
#view function,The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
arr=np.array([1,2,3,4,5])
arr2=arr.view()
arr[0]=42
print(arr)
print(arr2)
#The numpy.zeros() function is one of the most significant functions which is used in machine learning programs widely. This function is used to generate an array containing zeros.The numpy.zeros() function provide a new array of given shape and type, which is filled with zeros.
a=np.zeros((6,3))
print(a)
#The NumPy ones() function in Python is used to create an array of the specified shape and type, where all the elements are set to 1. This function is very similar to zeros(). The ones () function takes three arguments and returns the array filled with value 1. In this article, I will explain how to use the NumPy ones() function with examples.
a=np.ones((6,3))*9 # it multiply with ones at the diagonal
print(a)
#The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, upper, or lower depending on the optional parameter k. A positive k is for the upper diagonal, a negative k is for the lower, and a Øk (default) is for the main diagonal.
a=np.eye(4)
print(a)
#The diag tool returns a 2D array with input numbers as the diagonal and 0's elsewhere.
a=np.diag((3,4,5,6))
print(a)