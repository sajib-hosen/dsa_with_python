
# https://www.geeksforgeeks.org/python-data-structures-and-algorithms/ 

import numpy as np


def print_F(data):
    print(type(data), "==>", data)


# python list 
listOfName = ["sajib", "hosen"]
print_F(listOfName)

# 2d list 
twoD_list = [["name", 'address'], ['sajib', 'house 5']]
print_F(twoD_list)


tuple_list = ('Geeks', 'For') # kind of list
print_F(tuple_list) 


Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print_F(Set)

new_set = {'1text', 2, "new"}
print_F(new_set)

frozen_set = frozenset(["e", "f", "g"])
print_F(frozen_set)


string_new = 'This is python string'
print_F(string_new)

py_dict = {'Name': 'This is pytho dictionary', 1: [1, 2, 3, 4]}
print(py_dict['Name'])
print_F(py_dict)

# Matrix - need to understand
# Initial Array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)

# Printing a range of Array
# with the use of slicing method
sliced_arr = arr[:2, ::2]
print ("Array with first 2 rows and"
    " alternate columns(0 and 2):\n", sliced_arr)

# Printing elements at
# specific Indices
Index_arr = arr[[1, 1, 0, 3], 
                [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", Index_arr)


# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])
 
# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])

# Adding 1 to every element
print ("Adding 1 to every element:", a + 1)

# Subtracting 2 from each element
print ("\nSubtracting 2 from each element:", b - 2)

# sum of array elements
# Performing Unary operations
print ("\nSum of all array "
       "elements: ", a.sum())

# Adding two arrays
# Performing Binary operations
print ("\nArray sum:\n", a + b)

print("Integer Datatype: ")
print_F(a) 
print(a.dtype)

# Forced Datatype
x = np.array([1, 2], dtype = np.int64)   
print_F(x)
print(x.dtype)