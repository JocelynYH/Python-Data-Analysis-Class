
# coding: utf-8

# In[34]:

##
## File:           HW+2+Stat+3250+Jocelyn+Huang.py (STAT 3250)
## Topic:          Assignment 2
## Name:           Jocelyn Huang
## Section time:   3:30 - 4:45
## Grading Group:  3

#### Assignment 2, Part A
##
## A1. Generate an array x of 10000 random values from 
##     a uniform distribution on the interval [0,20],
##     then use a for loop to determine the percentage     
##     of values that are in the interval [5,12].

## Note: A1 asks for a percentage, not a count and not
##       a proportion.


x = np.random.uniform(low=0,high=20,size=10000)
ct = 0
for num in x:
    if 5 <= num <=12:
        ct += 1

print(ct)
print((ct/10000)*100)

'''
## A1. 
35.37%
'''


# In[38]:

## A2. Repeat A1 500 times, then compute the average
##     of the 500 percentages found.


percentages = np.empty(500)
for i in range(500):
    ct = 0
    per_ct = 0
    x = np.random.uniform(low=0,high=20,size=10000)
    for num in x:
        if 5 <=num<=12:
            ct += 1
            per_ct = ct/100
            
        percentages[i] = per_ct
print (np.mean(percentages))

'''
## A2. 
34.99%
'''


# In[47]:

## A3. For the array x in A1, use a while loop to determine 
##     the number of random entries required to find the
##     first that is less than 4.
x = np.random.uniform(low=0,high=20,size=10000)

cnt = 0
while x[cnt] >= 4:
    cnt += 1
    
print(cnt+1)

'''
## A3. 
4
'''


# In[53]:

## A4. Repeat A3 1000 times, then compute the average for the
##     number of random entries required.

avg = np.empty(1000)
for i in range(1000):
    x = np.random.uniform(low=0,high=20,size=10000)
    cnt = 0
    while x[cnt] >= 4:
        cnt += 1
    avg[i] = cnt + 1
print(np.mean(avg))

'''
## A4. 
5.25
'''


# In[70]:

## A5. For the array x in A1, use a while loop to determine 
##     the number of random entries required to find the
##     third entry that exceeds 12.

# trials = np.empty(2)
# for i in range(10000):
#     x = np.random.uniform(low=0,high=20,size=10000)
#     count = 0
#     while x[count] <= 12:
#         count += 1
#     trials[i] = count
# print(trials[2])

twelve_ct = 0 
ct = 0
x = np.random.uniform(low=0,high=20,size=10000)

while twelve_ct < 3:
    if x[ct] >= 12:
        twelve_ct += 1
    ct += 1

print(ct+1)

'''
## A5. 
12
'''


# In[82]:

## A6. Repeat A5 1000 times, then compute the average for the
##     number of random entries required.

#%%
container = np.empty(1000)
for i in range(1000):
    x = np.random.uniform(low=0,high=20,size=10000)
    twelve_ct = 0 
    ct = 0

    while twelve_ct < 3:
        if x[ct] >= 12:
            twelve_ct += 1
        ct += 1
        container[i] = ct + 1

print(np.mean(container))

'''
## A6. 
8.46
'''


# In[139]:

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
ct=0
for i in range(10000):
    s = np.random.choice(p1, size=10)
    ci_low = np.mean(s) - ((1.96*12)/np.sqrt(10))
    ci_high = np.mean(s) + ((1.96*12)/np.sqrt(10))
    if ci_low<40<ci_high:
        ct += 1
print("The proportion of confidence intervals that contain the population mean of 40, when n=10 is:",ct/10000)
    
    
#   ii) Repeat part i) using samples of size 20.
ct = 0 
for i in range(10000):
    s = np.random.choice(p1, size=20)
    ci_low = np.mean(s) - ((1.96*12)/np.sqrt(20))
    ci_high = np.mean(s) + ((1.96*12)/np.sqrt(20))
    if ci_low<40<ci_high:
        ct += 1
print("The proportion of confidence intervals that contain the population mean of 40, when n=20 is:",ct/10000)

#   iii) Repeat part i) using samples of size 30.
ct = 0 
for i in range(10000):
    s = np.random.choice(p1, size=30)
    ci_low = np.mean(s) - ((1.96*12)/np.sqrt(30))
    ci_high = np.mean(s) + ((1.96*12)/np.sqrt(30))
    if ci_low<40<ci_high:
        ct += 1
print("The proportion of confidence intervals that contain the population mean of 40, when n=30 is:",ct/10000)

'''
#B1 
The proportion of confidence intervals that contain the population mean of 40, when n=10 is: 0.9481
The proportion of confidence intervals that contain the population mean of 40, when n=20 is: 0.9499
The proportion of confidence intervals that contain the population mean of 40, when n=30 is: 0.9475
'''


# In[137]:

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
#     i)
ct=0
for i in range(10000):
    s = np.random.choice(p1, size=10)
    sample_st = np.std(s, ddof=1)

    ci_low = np.mean(s) - ((1.96*sample_st)/np.sqrt(10))
    ci_high = np.mean(s) + ((1.96*sample_st)/np.sqrt(10))
    if ci_low<40<ci_high:
        ct += 1
print("The proportion of confidence intervals that contain the population mean of 40, when n=10, is:",ct/10000)

#     ii)
ct=0
for i in range(10000):
    s = np.random.choice(p1, size=20)
    sample_st = np.std(s, ddof=1)

    ci_low = np.mean(s) - ((1.96*sample_st)/np.sqrt(20))
    ci_high = np.mean(s) + ((1.96*sample_st)/np.sqrt(20))
    if ci_low<40<ci_high:
        ct += 1
print("The proportion of confidence intervals that contain the population mean of 40, when n=20, is:",ct/10000)


#     iii)
ct=0
for i in range(10000):
    s = np.random.choice(p1, size=30)
    sample_st = np.std(s, ddof=1)

    ci_low = np.mean(s) - ((1.96*sample_st)/np.sqrt(30))
    ci_high = np.mean(s) + ((1.96*sample_st)/np.sqrt(30))
    if ci_low<40<ci_high:
        ct += 1
print("The proportion of confidence intervals that contain the population mean of 40, when n=30, is:",ct/10000)


'''
#B2
The proportion of confidence intervals that contain the population mean of 40, when n=10, is: 0.919
The proportion of confidence intervals that contain the population mean of 40, when n=20, is: 0.9336
The proportion of confidence intervals that contain the population mean of 40, when n=30, is: 0.9423
'''


# In[134]:

#  c) Your answers in part b) should be a bit off.  The 
#     problem is that a t-distribution is appropriate when
#     using the sample standard deviation.  Repeat part b),
#     this time using t* in place of 1.96 in the formula,
#     where: t* = 2.262 for n = 10, t* = 2.093 for n = 20,
#     and t* = 2.045 for n = 30.

#     i)
ct=0
for i in range(10000):
    s = np.random.choice(p1, size=10)
    sample_st = np.std(s, ddof=1)

    ci_low = np.mean(s) - ((2.262*sample_st)/np.sqrt(10))
    ci_high = np.mean(s) + ((2.262*sample_st)/np.sqrt(10))
    if ci_low<40<ci_high:
        ct += 1
print("The proportion of confidence intervals that contain the population mean of 40, when n=10, is:",ct/10000)

#     ii)
ct=0
for i in range(10000):
    s = np.random.choice(p1, size=20)
    sample_st = np.std(s, ddof=1)

    ci_low = np.mean(s) - ((2.093*sample_st)/np.sqrt(20))
    ci_high = np.mean(s) + ((2.093*sample_st)/np.sqrt(20))
    if ci_low<40<ci_high:
        ct += 1
print("The proportion of confidence intervals that contain the population mean of 40, when n=20, is:",ct/10000)


#     iii)
ct=0
for i in range(10000):
    s = np.random.choice(p1, size=30)
    sample_st = np.std(s, ddof=1)

    ci_low = np.mean(s) - ((2.045*sample_st)/np.sqrt(30))
    ci_high = np.mean(s) + ((2.045*sample_st)/np.sqrt(30))
    if ci_low<40<ci_high:
        ct += 1
print("The proportion of confidence intervals that contain the population mean of 40, when n=30, is:",ct/10000)

'''
#B3
The proportion of confidence intervals that contain the population mean of 40, when n=10, is: 0.919
The proportion of confidence intervals that contain the population mean of 40, when n=20, is: 0.9336
The proportion of confidence intervals that contain the population mean of 40, when n=30, is: 0.9423
'''


# In[ ]:



