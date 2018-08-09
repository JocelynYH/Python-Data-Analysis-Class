##
## File: assignment01.py (STAT 3250)
## Topic: Assignment 1
##

#### Assignment 1, Part A
##
## For the questions in this part, use the following
## lists as needed:
mylist01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
mylist02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1]

## A1. Find the last four digits of the 13th Mersenne
##     prime, which is equal to 2^521 - 1.

## A2. Find the product of the 7th entry in mylist01,
##     the 13th entry in mylist01, and the 4th entry
##     in mylist02.

## A3. Extract the sublist of mylist02 that goes from
##     the 5th to the 9th elements (inclusive).

## A4. Concatenate mylist01 to mylist02, sort the new
##     combined list, then extract the sublist that 
##     goes from the 8th to the 19th elements (inclusive).

## A5. Determine the number of times 8 appears in the 
##     combined list in A4.

## A6. Create a new list be removing all of the 3's from
##     mylist01.

## A7. Extract a sublist of mylist02 consisting of every
##     3rd entry, starting at the end and going in 
##     reverse.

## A8. From the combined list in A4, extract a sublist of
##     every 5th entry, starting with the 3rd entry.

#%%

#### Assignment 1, Part B
##
## For the questions in this part, use the following
## lists as needed:
mylist01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
mylist02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1]

## B1. Use a for loop to add up the cubes of the entries
##     of mylist01.

## B2. Use a for loop to create mylist03, which has 15
##     entries, each the product of the corresponding 
##     entry from mylist01 multiplied by the corresponding
##     entry from mylist02.  That is,
##     mylist03[i] = mylist01[i]*mylist02[i] 
##     for each 0 <= i <= 14.

## B3. Use a for loop to compute the mean of the entries
##     of mylist02.  (Hint: len(mylist02) gives the number
##     of entries in mylist.  This is potentially useful.)


#%%

#### Assignment 1, Part C
##
## For the questions in this part, use the following
## lists as needed:
mylist01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
mylist02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1]
mylist03 = [2,-5,6,7,-2,-3,0,3,0,2,8,7,9,2,0,-2,5,5,6]
biglist = mylist01 + mylist02 + mylist03

## C1. Use a for loop to determine the number of entries
##     in "biglist" that are greater than 4.

## C2. Use a for loop to determine the number of entries
##     in "biglist" that are between -1 and 3 (inclusive).

## C3. Create a new list called "mylist04" that contains 
##     the elements of biglist that are not divisible by 3.


#%%









