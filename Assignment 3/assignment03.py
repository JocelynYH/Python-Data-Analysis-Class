##
## File: assignment03.py (STAT 3250)
## Topic: Assignment 3
##

#### Assignment 3, Part A
##
## The problems in Part A should be done without the use of 
## loops.  They can be done with NumPy functions.

## The different questions in this part use the array
## defined below.

import numpy as np # Load NumPy
arr1 = np.array([[2,5,3,-1,0,1,-6,8,1,-9],[-1,3,4,2,0,1,2,7,8,-1],
                [3,0,-2,-2,5,4,8,-1,0,2],[3,3,-3,2,4,5,1,9,8,6],
                [1,1,0,2,-3,-2,4,-7,0,-9],[0,1,7,8,-5,-4,0,2,5,-9]])

##  (a) Extract a submatrix arr1_slice1 from arr1 that consists of
##      the second and third rows of arr1.
##  (b) Find a one dimensional array that contains the entries of
##      arr1 that are less than -5.
##  (c) Determine the number of entries of arr1 that are greater
##      than 3
##  (d) Find the mean of the entries of arr1 that are less than
##      or equal to -2.
##  (e) Find the sum of the squares of the even entries of arr1.
##  (f) Determine the proportion of positive entries of arr1 
##      that are greater than 3.

#%%

#### Assignment 3, Part B
##
## The problems in Part B should be done without the use of 
## loops.  They can be done with NumPy functions.

## Use the code below to define arr2 and arr3

arr2 = np.arange(-20,28,2)
arr2 = arr2.reshape((4,6))
arr3 = np.arange(-20,12)
arr3 = arr3.reshape((8,4))

##  (a) Extract a submatrix from arr2 of elements that are
##      in rows 0 and 3 and columns 1 and 4 of arr2, then
##      determine the mean and standard deviation of
##      those elements.
##  (b) Multiply each element of arr2 by 3, then add 1
##      to each element, then replace the even values
##      of the resulting matrix with 0. 
##  (c) Extract rows 1 and 6 from arr3, find the transpose
##      of the resulting matrix.
##  (d) Replace the odd negative entries of arr3 with zeros,
##      then determine the means of the rows of the
##      resulting matrix.
##  (e) Find all entries that are in both arr2 and arr3.
##  (f) Find all entries that are in arr3 but not arr2.

#%%


#### Assignment 3, Part C

## C1. Suppose that course grades are assigned based on
##     course average as follows: 90's = A, 80's = B,
##     70's = C, 60's = D, Below 60 = F.
##     
##  (i) Define a function called "grade" that takes a course
##      average as input and returns a grade.
##  (ii) Use a for loop to take the list of course averages
##       defined below and convert it into a list of
##       corresponding course grades. 

[99, 73, 60, 91, 93, 92, 68, 55, 60, 79, 79, 92, 51, 78, 68, 90, 99,
       62, 58, 76, 78, 65, 92, 83, 95, 82, 92, 85, 83, 65, 85, 61, 69, 72,
       63, 79, 59, 63, 85, 97]





