
# coding: utf-8

# In[73]:

##
## File:           assignment01.py (STAT 3250)
## Topic:          Assignment 1
## Name:           Jocelyn Huang
## Section time:   3:30 - 4:45
## Grading Group:  3

#### Assignment 1, Part A
##
## For the questions in this part, use the following
## lists as needed:
mylist01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
mylist02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1]
print(mylist01)
print(mylist02)


# In[75]:

## A1. Find the last four digits of the 13th Mersenne
##     prime, which is equal to 2^521 - 1.

print(2**521 -1)
'''
#A1
7151
'''


# In[76]:

## A2. Find the product of the 7th entry in mylist01,
##     the 13th entry in mylist01, and the 4th entry
##     in mylist02.

print(mylist01[6]*mylist01[12]*mylist02[3])

'''
#A2
-75
'''


# In[80]:

## A3. Extract the sublist of mylist02 that goes from
##     the 5th to the 9th elements (inclusive).

(mylist02[4:9])


'''
#A3
[-5, -2, 4, 6, 7]
'''

## if [a:n], stops before n


# In[84]:

## A4. Concatenate mylist01 to mylist02, sort the new
##     combined list, then extract the sublist that 
##     goes from the 8th to the 19th elements (inclusive).

mybiglist = mylist01+mylist02
print(mybiglist)

mybiglist.sort()
print(mybiglist)

mybiglist[7:19]

'''
#A4
[-3, -3, -2, -2, 0, 0, 1, 2, 2, 2, 3, 3]
'''


# In[85]:

## A5. Determine the number of times 8 appears in the 
##     combined list in A4.

mybiglist.count(8)

'''
#A4
3
'''


# In[86]:

## A6. Create a new list be removing all of the 3's from
##     mylist01.

print(mylist01)

without3 = list(mylist01)

for element in without3:
    if element == 3:
        without3.remove(3)
        
# i = 0
# for i in range(len(without3)):
#     if element == 3:
#         without3[i].remove(3)
    
# y = 0
# while y < len(without3):
#     if elment == 3:
#         without3[y].remove(3)
#     y = y + 1

   

print(without3)
print(mylist01)

'''
#A5
[2, 5, 4, 9, 10, -3, 5, 5, -8, 0, 2, 8, 8, -2, -4, 0, 6]
'''


# In[87]:

## A7. Extract a sublist of mylist02 consisting of every
##     3rd entry, starting at the end and going in 
##     reverse.

mylist02[::-3]

'''
#A6
[1, 13, 9, 6, -5, -3]
'''


# In[89]:

## A8. From the combined list in A4, extract a sublist of
##     every 5th entry, starting with the 3rd entry.

print(mybiglist)
mybiglist[2::5]

'''
#A8
[-7, -3, 0, 3, 5, 7, 9]
'''

#%%


# In[56]:

#### Assignment 1, Part B
##
## For the questions in this part, use the following
## lists as needed:
mylist01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
mylist02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1]


# In[90]:

## B1. Use a for loop to add up the cubes of the entries
##     of mylist01.
cubesum = 0 
for x in mylist01:
    cubesum += x**3

print(cubesum)

'''
#B1
2867
'''


# In[58]:

## B2. Use a for loop to create mylist03, which has 15
##     entries, each the product of the corresponding 
##     entry from mylist01 multiplied by the corresponding
##     entry from mylist02.  That is,
##     mylist03[i] = mylist01[i]*mylist02[i] 
##     for each 0 <= i <= 14.

mylist03 = 15*[0]
for i in range(15):
    mylist03[i] = mylist01[i]*mylist02[i]     

print(mylist03)

'''
#B2
[-14, -15, 32, -45, -50, 6, 20, 30, 21, -40, 0, 20, 6, 104, -96]
'''


# In[59]:

## B3. Use a for loop to compute the mean of the entries
##     of mylist02.  (Hint: len(mylist02) gives the number
##     of entries in mylist.  This is potentially useful.)
x = 0
print(mylist02)
for i in mylist02:
    x = i + x
print(x)
length = len(mylist02)
print(length)
average = x/length
print(average)

'''
#B3
1.588235294117647
'''
#%%


# In[60]:

#### Assignment 1, Part C
##
## For the questions in this part, use the following
## lists as needed:
mylist01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
mylist02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1]
mylist03 = [2,-5,6,7,-2,-3,0,3,0,2,8,7,9,2,0,-2,5,5,6]
biglist = mylist01 + mylist02 + mylist03


# In[61]:

## C1. Use a for loop to determine the number of entries
##     in "biglist" that are greater than 4.
entries = 0
for i in biglist:
    if i > 4:
        entries = entries + 1
print(entries)
        
'''
#C1
23
'''


# In[64]:

## C2. Use a for loop to determine the number of entries
##     in "biglist" that are between -1 and 3 (inclusive).
entriesbtwn = 0
for i in biglist:
    if -1<=i<=3:
        entriesbtwn = entriesbtwn +1
print(entriesbtwn)

'''
#C2
15
'''


# In[66]:

## C3. Create a new list called "mylist04" that contains 
##     the elements of biglist that are not divisible by 3.
mylist04 = list()
for i in biglist:
    if i % 3 != 0:
        mylist04.append(i)
        
print(mylist04)

'''
#C3
[2, 5, 4, 10, 5, 5, -8, 2, 8, 8, -2, -4, -7, 8, -5, -5, -2, 4, 7, 5, 10, 2, 13, -4, 1, 2, -5, 7, -2, 2, 8, 7, 2, -2, 5, 5]
'''

#%%


# In[ ]:



