##
## File: assignment05b.py (STAT 3250)
## Topic: Assignment 5b
##

## NOTE: This is the second part of Assignment 5.  Please submit your
##       answers in a *single* Python file.

#### Part 2
##
## The questions in Part 2 refer to the data in the file
## 'fastfood3.csv'.  This file has the columns in 'fastfood2.csv'
## plus a new column 'satisfaction'.  This new column gives the
## customer's satisfaction on a scale of 1-10 (10 being most satisfied)

##  (a) What percentage of customers gave the highest possible satisfaction 
#       rating?  What percentage gave the lowest rating?
##  (b) Determine the mean satisfaction for each day of the week.
##  (c) The company considers a satisfaction rating of 7 or higher 
##      to indicate a "satisfied" customer.  Find a 95% confidence interval
##      for the proportion of satisfied customers for each of Breakfast,
##      Lunch, and Dinner.  
##  (d) The company suspects that the time required to fill an order can
##      influence customer satisfaction.  Find a 95% confidence interval
##      for the proportion of satisfied customers among those whose orders
##      took no more than 180 seconds to fill.  Do the same for those
##      whose orders too at least 360 seconds to fill.
##  (e) Company analysts have developed a formula for predicting customer
##      satisfaction ratings.  It is
##
##         predicted satisfaction= 4 + 0.002*cost - 0.005*secs + m,
##
##      where m = 1 if the meal is Breakfast, and 0 otherwise.
##
##      Predict each customer's satisfaction based on this formula, and
##      add this prediction as a new column on the data frame named
##      "predsatis".  Then compute the mean predicted rating.
##  (f) For all the customers, find the maximum difference between the 
##      predicted satisfaction rating and the actual satisfaction rating.
##      (This should be the absolute value of the difference.)  Do the same
##      for the minimum difference, and then find the average of all the
##      differences.
