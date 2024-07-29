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
#printing diagonal elements from exisiting array
arr=np.array([[1,2,3],[4,5,6],[2,4,6]])
print(np.diag(arr))
#Slicing Array
arr=np.array([1,2,3,4,5,6,7,8])
print(arr[1:5:2])
#randint() is an inbuilt function of the randon module in Python3. The random module gives access to various useful functions one of them being able to generate random numbers, which is randint()
rand = np.random.rand(4)
print(rand)
rand = np.random.rand(2,3)
print(rand)
arr= np.random.randint(0,10,10)
print(arr)
#The reshape Function in Rusly allows you to change the shape (dimensions) of an array without changing Its data. This can be useful when you want to rearrange the way data is organized in an array, such as converting a 1-dimensional array inte a 2-dimensional matrix or vice versa, or changing the tle of a multi-dimensional array while saintaining the total number of elements.
arr = np.random.randint(0,100,12)
print(arr)
arr=arr.reshape(4,3)
print(arr)
print("Array Value ",arr[0][1])
print(arr.shape)
arr=arr.reshape(-1,4)
print(arr)
arr=arr.reshape(2,-1)
print(arr)
#seed()
np.random.seed(145)
arr=np.random.randint(0,100,12)
print(arr)
#slicing
np.random.seed(111)
arr=np.random.randint(0,500,30)
arr=arr.reshape(6,5)
print(arr)
print(arr[2:,2:])
print(arr[3:5,2:4])
#arange
ar=np.arange(1,15)
print(ar)
print(ar[ar%2!=0])
arr=np.arange(1,8)
print(arr+2)
print(arr*2)
print(arr**2)
#Mathematical Functions
arr=np.array([10,20,30,25,6,2])
print(np.min(arr))
print(np.max(arr))
print(np.argmax(arr))
print(np.argmax(arr))
print(np.sqrt(arr))

np.random.seed (122)

mat =np.random.randint(1,21,9).reshape(3,3)
print(mat)
print(np.sum (mat))
print (np.cumsum(mat))
print(np.min (mat))
print(np.max(mat))
print("----------")
print(np.sum (mat, axis=1))
print(np. min (mat,axis=1))
print (np. max(mat,axis=1))
print(np.cumsum(mat,axis=1))
#Unique() 
np.random.seed(122)
mat = np.random.randint(1, 21, 9)
print(mat)
np.random.shuffle(mat)
print(mat)
print(np.unique(mat,return_index=True,return_counts=True))
print(np.unique(mat).size)
#np.transpose is used to transpose or permute the dimensions of an array. It swaps rows and columns.
mat=np.array([1,2,3,4,5,6])
print(np.transpose(mat))
# search the index of a value 
search = np.searchsorted(mat,4)
print(search)
print("***********split***************")
#np.split()
arr= np.array([1,2,3,4,5,6])
sub_array=np.split(arr,3)
for sub_arr in sub_array:
    print(sub_arr)
print("************")
#Splitting with Specified Indices:
arr = np.array([1, 2, 3, 4, 5, 6])
sub_arrays = np.split(arr, [2, 4])
for sub_arr in sub_arrays:
    print(sub_arr)
print("*******************")
#Splitting Along Different Axis (Columns):
matrix = np.array([[1, 2, 3],
[4, 5, 6]])
sub_matrices = np.split(matrix, 3, axis=1)
for sub_matrix in sub_matrices:
 print(sub_matrix)
print("****************************")
# concatenating along rows (vertical concatenation):
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
# Concatenate arr1 and arr2 along rows (vertical)
result = np.concatenate((arr1, arr2), axis=0)
print(result)
print("******************************")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5], [6]])
# Concatenate arr1 and arr2 along columns (horizontal)
result = np.concatenate((arr1, arr2), axis=1)
print(result)
print("***********")
#np.vstack
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# Stack arr1 and arr2 vertically
result = np.vstack((arr1, arr2))
print(result)
print("*************************")
#np.hstack
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# Stack arr1 and arr2 vertically
result = np.hstack((arr1, arr2))
print(result)
# Calculate the Mean First, you calculate the mean (average) scores for each class.   
classA= np.array([85, 88, 90, 92, 95])
classA_mean=np.mean(classA)
print('Class A Score Average',classA_mean )
vari = np.var(classA)
print("class a variance is ",vari)
std=np.std(classA)
print("class a variance is ",std)
print("**************************")
#percentile
test_scores = np.array([65, 75, 80, 85, 90, 92, 94, 95, 96, 98, 100, 102, 104, 106, 108,
110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138])
median = np.percentile(test_scores, 50)
print(median)
#Saving and Loading NumPy Arrays
scores = np.array([85, 92, 78, 88, 95, 72, 89])
np.save('student_scores.npy', scores)
loaded_scores = np.load('student_scores.npy')
print("Original Scores:", scores)
print("Loaded Scores:", loaded_scores)