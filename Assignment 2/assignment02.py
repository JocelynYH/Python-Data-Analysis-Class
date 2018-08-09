##
## File: assignment02.py (STAT 3250)
## Topic: Assignment 2
##

#### Assignment 2, Part A
##
## A1. Generate an array x of 10000 random values from 
##     a uniform distribution on the interval [0,20],
##     then use a for loop to determine the percentage     
##     of values that are in the interval [5,12].

## Note: A1 asks for a percentage, not a count and not
##       a proportion.

## A2. Repeat A1 500 times, then compute the average
##     of the 500 percentages found.

## A3. For the array x in A1, use a while loop to determine 
##     the number of random entries required to find the
##     first that is less than 4.

## A4. Repeat A3 1000 times, then compute the average for the
##     number of random entries required.

## A5. For the array x in A1, use a while loop to determine 
##     the number of random entries required to find the
##     third entry that exceeds 12.

## A6. Repeat A5 1000 times, then compute the average for the
##     number of random entries required.

#%%


#### Assignment 2, Part B
##

#    For this problem you will draw samples from a normal
#    population with mean 40 and standard deviation 12.
#    Run the code below to generate your population, which
#    will consist of 500,000 elements.

import numpy as np 
p1 = np.random.normal(40,12,size=500000)

#  a) The formula for a 95% confidence interval for the 
#     population mean is given by
#     
#     [xbar - 1.96*sigma/sqrt(n), xbar + 1.96*sigma/sqrt(n)]
#
#     where xbar is the sample mean, sigma is the population
#     standard deviation, and n is the sample size.
#
#   i) Select 10,000 random samples of size 10 from p1.  For
#      each sample, find the corresponding confidence 
#      interval, and then determine the proportion of
#      confidence intervals that contain the population mean.
#   ii) Repeat part i) using samples of size 20.
#   iii) Repeat part i) using samples of size 30.
#
#  b) Frequently in applications the population standard
#     deviation is not known. In such cases, the sample
#     standard deviation is used instead.  Repeat part a)
#     replacing the population standard deviation with the
#     standard deviation from each sample, so that the
#     formula is
#
#     [xbar - 1.96*stdev/sqrt(n), xbar + 1.96*stdev/sqrt(n)]
#
#     Tip: The command for the standard deviation is 
#          np.std(data, ddof=1)
#
#  c) Your answers in part b) should be a bit off.  The 
#     problem is that a t-distribution is appropriate when
#     using the sample standard deviation.  Repeat part b),
#     this time using t* in place of 1.96 in the formula,
#     where: t* = 2.262 for n = 10, t* = 2.093 for n = 20,
#     and t* = 2.045 for n = 30.










