
# coding: utf-8

# In[5]:

##
## File:           HW+3+STAT+3250+Jocelyn+Huang.py (STAT 3250)
## Topic:          Assignment 3
## Name:           Jocelyn Huang
## Section time:   3:30 - 4:45
## Grading Group:  3

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
arr1_slice1 = arr1[[1,2]]
print(arr1_slice1)


'''
#Aa
[[-1  3  4  2  0  1  2  7  8 -1]
 [ 3  0 -2 -2  5  4  8 -1  0  2]]
'''


# In[6]:

##  (b) Find a one dimensional array that contains the entries of
##      arr1 that are less than -5.
arr1[arr1<-5]
'''
#Ab
array([-6, -9, -7, -9, -9])
'''


# In[7]:

##  (c) Determine the number of entries of arr1 that are greater
##      than 3
(arr1>3).sum()
'''
#Ac
17
'''


# In[8]:

##  (d) Find the mean of the entries of arr1 that are less than
##      or equal to -2.

arr1[arr1 <= -2].mean()
'''
#Ad
-5.083333333333333
'''


# In[9]:

##  (e) Find the sum of the squares of the even entries of arr1.
np.sum(arr1[arr1 %2 == 0]**2)

'''
#Ae
512
'''


# In[10]:

##  (f) Determine the proportion of positive entries of arr1 
##      that are greater than 3.

((arr1 > 3).sum())/((arr1 > 0).sum())


'''
#Af
0.47222222222222221
'''

#%%


# In[11]:

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
sub_arr2 = arr2[[0,3]][:,[1,4]]
np.mean(sub_arr2)
np.std(sub_arr2)

'''
#Ba
mean:   3.0
st-dev: 18.248287590894659
'''
print(arr2)


# In[12]:

##  (b) Multiply each element of arr2 by 3, then add 1
##      to each element, then replace the even values
##      of the resulting matrix with 0. 
modified_arr2 = (arr2*3)+1
print(modified_arr2)


# In[13]:

np.where(modified_arr2 % 2 ==0, 0, modified_arr2)
'''
#Bb
array([[-59, -53, -47, -41, -35, -29],
       [-23, -17, -11,  -5,   1,   7],
       [ 13,  19,  25,  31,  37,  43],
       [ 49,  55,  61,  67,  73,  79]])
'''


# In[70]:

##  (c) Extract rows 1 and 6 from arr3, find the transpose
##      of the resulting matrix.

arr3[[1,6]].T
'''
#Bc
array([[-16,   4],
       [-15,   5],
       [-14,   6],
       [-13,   7]])
'''


# In[66]:

##  (d) Replace the odd negative entries of arr3 with zeros,
##      then determine the means of the rows of the
##      resulting matrix.
replace_arr3 = np.where(np.logical_and(arr3<0, arr3 % 2 != 0), 0, arr3)
print(replace_arr3)
replace_arr3.mean(axis=1)
'''
#Bd
array([-9.5, -7.5, -5.5, -3.5, -1.5,  1.5,  5.5,  9.5])
'''


# In[36]:

##  (e) Find all entries that are in both arr2 and arr3.
np.intersect1d(arr2,arr3)

'''
#Be
array([-20, -18, -16, -14, -12, -10,  -8,  -6,  -4,  -2,   0,   2,   4,
         6,   8,  10])
'''


# In[37]:

##  (f) Find all entries that are in arr3 but not arr2.
np.setdiff1d(arr3,arr2)
'''
#Bf
array([-19, -17, -15, -13, -11,  -9,  -7,  -5,  -3,  -1,   1,   3,   5,
         7,   9,  11])
'''
#%%


# In[56]:

#### Assignment 3, Part C

## C1. Suppose that course grades are assigned based on
##     course average as follows: 90's = A, 80's = B,
##     70's = C, 60's = D, Below 60 = F.
##     
##  (i) Define a function called "grade" that takes a course
##      average as input and returns a grade.

def grade (x):
    if x >=90:
        return("A")
    elif 90>x>=80:
        return("B")
    elif 80>x>=70:
        return("C")
    elif 70>x>=60:
        return("D")
    else:
        return("F")


# In[59]:

##  (ii) Use a for loop to take the list of course averages
##       defined below and convert it into a list of
##       corresponding course grades. 


list_grades = [99, 73, 60, 91, 93, 92, 68, 55, 60, 79, 79, 92, 51, 78, 68, 90, 99,
       62, 58, 76, 78, 65, 92, 83, 95, 82, 92, 85, 83, 65, 85, 61, 69, 72,
       63, 79, 59, 63, 85, 97]


for i in range(len(list_grades)):
    list_grades[i] = grade(list_grades[i])
print(list_grades)    

'''
#Cii
['A', 'C', 'D', 'A', 'A', 'A', 'D', 'F', 'D', 'C', 'C', 'A', 'F', 'C', 'D', 'A', 'A', 'D', 'F', 'C', 'C', 'D', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'D', 'B', 'D', 'D', 'C', 'D', 'C', 'F', 'D', 'B', 'A']
'''


# In[ ]:



