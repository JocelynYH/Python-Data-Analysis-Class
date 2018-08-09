
# coding: utf-8

# In[137]:

##
## File:           HW+12+Stat+3250+Jocelyn+Huang.py (STAT 3250)
## Topic:          Assignment 12
## Name:           Jocelyn Huang
## Section time:   3:30 - 4:45
## Grading Group:  3

#### Assignment 12
##

## 1. Suppose $50,000 is invested on the investor's 40th birthday at a fixed rate of return
## mu = 7.6% continuous. Determine the account balance each year from until the investor's 
## 65th birthday, and printa table that shows the investor's age and the investment balance
import numpy as np # import necessary packages
import pandas as pd
mu = .076 # set mu
balance = [] # initialize empty list
Bi=50000 # set balance

for i in range(40,66):   # for loop through out each age
    balance.append(Bi)   # add balance to list
    Bi = np.exp(mu)*Bin  # calculate increase in balance w/ formula
balance = np.round(balance, 2)  # round the list
len(balance)  # double check to make sure the list is at the appropriate length


table = pd.DataFrame(columns={'Balance'}, index=(range(40,66))) # create a dataframe with empty balance column
table.index.name = 'Age' # use index as age
table['Balance']=balance  # fill df with balance data
table
'''
#1
    Balance
Age	
40	50000.00
41	53948.13
42	58208.01
43	62804.27
44	67763.45
45	73114.23
46	78887.52
47	85116.68
48	91837.71
49	99089.45
50	106913.81
51	115356.00
52	124464.81
53	134292.87
54	144896.98
55	156338.42
56	168683.30
57	182002.97
58	196374.39
59	211880.62
60	228611.26
61	246662.99
62	266140.14
63	287155.25
64	309829.77
65	334294.72
'''


# In[233]:

# 2. Suppose we have the same investment as in the previous question, except that the 
# annual rate of return has a lognormal distribution with mean mu = 7.6% and standard 
# deviation sigma = 16.7%. Simulate 100,000 times the balance on the investor's 65th birthday, 
# then use the results to answer the following questions regarding these balances:

# (a) What is the mean balance?
mu2 = .076  # redefine mu
sigma2 = .167 # define sigma
Bi = 50000    # reset balance

iterations = []  # empty list to hold each value at 65
for x in range(1,100001):  # for loop to iterate 100k times
    Bi=50000               # each run through, redefine balance
    for i in range(1,27):  # this set is run 100k times and simulates one lifetime
        Bi = np.exp(np.random.normal(mu2, sigma2, 1))*Bi  # different equation uses sigma and is more random
    Bi=np.asscalar(Bi)     # converts so we can append to list
    iterations.append(Bi)  # append ending values to iterations list
iterations    # check it out

sampmu2 = np.round(np.mean(iterations),2)  # calculate and print and round mean of the simulations
print("%.2f" % sampmu2) 
'''
#2a
516556.26
'''

# (b) What is the median balance?  # calculate and print and round mean of the simulations
median2 = np.round(np.median(iterations),2)
print("%.2f" % median2) 
'''
#2b
361367.26
'''


# In[234]:

# (c) Give a 95% confidence interval for the balance. (That is, find the range of balances 
# that make up the middle 95% of simulated balances.)
iterations.sort() # sort the data of simulated balances
print("The Confidence Interval is", iterations[4999],",",iterations[-4999])  # pull the numbers in the place of the 5th% and 95th% values
'''
#2c
The Confidence Interval is 89656.83735703288 , 1460545.7382616312
'''


# In[161]:

# (d) The investor's goal is to have a 65th-birthday balance of at least $300,000. What proportion of
# times was the investor successful?
x=0   # initialize counter
for i in iterations:  # a for loop, which counts the number of balances over 300k
    if i >= 300000:
        x+=1         # if vaue is equal or over to 300k, add a count
print(x/100000)  # print the count over total values
'''
#2d
The proportion of success was 0.58608.
'''

# (e) Plot a histogram of balances from this simulation.
import matplotlib.pyplot as plt # import necessary package

plt.hist(iterations, bins=200, range=[0, 2500000]) # plot over the given range
'''
#2e
See attached.'''


# In[136]:

# 3
# Repeat question 1, but now suppose that in addition to the initial deposit of $50,000 on the investor's
# 40th birthday, there are also deposits of $3000 made on each birthday 41, 42, ..., 65. Assuming a
# fixed rate of return mu = 7:6% continuous as before, and the balance on the investor's 65th birthday,
# immediately after the last deposit. Make a table of the birthdays from 40 to 65, and the balances. The
# first three table entries are below.
 
mu3 = .076 # same as before
balance3 = []
Bi=50000

for i in range(40,66):  # same as before, but 
    balance3.append(Bi)
    Bi = (np.exp(mu)*Bi) + 3000  # add the 3k deposit each year
balance3 = np.round(balance3, 2)
len(balance3)


np.round(balance3, 2) # same as before
table3 = pd.DataFrame(columns={'Age','Balance'}, index=(range(40,66)))
# table3['Age']=range(40,66)
table3.index.name = 'Age'
table3=table3.drop('Age',1)
table3['Balance']=balance3
table3
'''
#3
	Balance
Age	
40	50000.00
41	56948.13
42	64444.90
43	72533.63
44	81261.08
45	90677.66
46	100837.80
47	111800.22
48	123628.25
49	136390.25
50	150159.98
51	165017.00
52	181047.16
53	198343.11
54	217004.80
55	237140.05
56	258865.24
57	282305.91
58	307597.51
59	334886.20
60	364329.68
61	396098.09
62	430375.01
63	467358.53
64	507262.36
65	550317.10
'''


# In[186]:

# 4.
# Repeat question 2, but now suppose that in addition to the initial deposit of $50,000 on the investor's
# 40th birthday, there are also deposits of $3000 made on each birthday 41, 42, ..., 65. Assume the annual
# rate of return has a lognormal distribution with mean mu = 7.6% and standard deviation sigma= 16.7%, and
# simulate 100,000 times the balance on the investor's 65th birthday immediately after the last deposit.
# Use the simulations to answer (a)-(e).

# (a) What is the mean balance?

Bi = 50000

iterations3 = []
for x in range(1,100001):
    Bi=50000
    for i in range(1,27):   # same as before (with random variation), but add the deposit
        Bi = (np.exp(np.random.normal(mu2, sigma2, 1))*Bi)+3000
    Bi=np.asscalar(Bi)
    iterations3.append(Bi)
iterations3

sampmu2 = np.round(np.mean(iterations3),2)
print("%.2f" % sampmu2)
'''
#4a
817157.12
'''

# (b) What is the median balance?
median2 = np.round(np.median(iterations3),2)
print("%.2f" % median2) 
'''
#4b
608643.91
'''

# (c) Give a 95% confidence interval for the balance. (That is, find the range of balances 
# that make up the middle 95% of simulated balances.)
iterations3.sort()
print("The Confidence Interval is", iterations3[4999],",",iterations3[-4999])
'''
#4c
The Confidence Interval is 195198.28842831394 , 2109734.604538135
'''

# (d) The investor's goal is to have a 65th-birthday balance of at least $300,000. What proportion of
# times was the investor successful?
x=0
for i in iterations3:
    if i >= 300000:
        x+=1
print(x/100000)
'''
#4d
The proportion of success was 0.8409.
'''

# (e) Plot a histogram of balances from this simulation.
plt.hist(iterations3, bins=200, range=[0, 3500000]) 
'''
#4e
see attached.
'''


# In[244]:

# 5. Now let's factor inflation. Repeat question 3, but suppose that the birthday deposits start at $3000
# on the 41st birthday, and increase by 3% continuous each year until the 65th birthday, so that the
# 42nd-birthday is $3000e:03 = $3091:36, the 43rd-birthday deposit is $3091:36e:03 = $3185:51, and so
# on. Make a table of the birthdays from 40 to 65, and the balances. The first three table entries are
# below.

balance5 = []
Bi=50000

deposit=3000

for i in range(40,66):  # same as before, except for each year:
    balance5.append(Bi)
    Bi = (np.exp(mu)*Bi) + deposit
    deposit = deposit*np.exp(.03)  # deposit is increased by the exponential formula
balance5 = np.round(balance5, 2)
len(balance5)

np.round(balance5, 2)
table5 = pd.DataFrame(columns={'Balance'}, index=(range(40,66)))
# table3['Age']=range(40,66)
table5.index.name = 'Age'
table5['Balance']=balance5
print(table5)
'''
#5
	Balance
Age	
       Balance
Age           
40    50000.00
41    56948.13
42    64536.26
43    72817.72
44    81850.12
45    91695.71
46   102421.74
47   114100.87
48   126811.61
49   140638.73
50   155673.82
51   172015.80
52   189771.51
53   209056.35
54   229994.92
55   252721.79
56   277382.29
57   304133.33
58   333144.36
59   364598.32
60   398692.74
61   435640.90
62   475673.06
63   519037.80
64   566003.51
65   616859.91
'''


# In[ ]:

# 6. Repeat question 4, but suppose that the birthday deposits start at $3000 on the 41st birthday, and
# increase by 3% continuous each year until the 65th birthday as in 5. Use the simulations to answer
# (a){(e).


# (a) What is the mean balance?
mu2 = .076
sigma2 = .167

iterations6 = []
for x in range(1,100001):    # same as before, but deposit is increased. 
    Bi=50000
    deposit=3000
    for i in range(1,27):
        Bi = (np.exp(np.random.normal(mu2, sigma2, 1))*Bi)+deposit
        deposit = deposit*np.exp(.03)
    Bi=np.asscalar(Bi)
    iterations6.append(Bi)
iterations6

sampmu5 = np.round(np.mean(iterations6),2)
print("%.2f" % sampmu5)
'''
#6a
900100.84
'''

# (b) What is the median balance?
median2 = np.round(np.median(iterations6),2)
print("%.2f" % median2) 
'''
#6b
689941.21
'''

# (c) Give a 95% confidence interval for the balance. (That is, find the range of balances 
# that make up the middle 95% of simulated balances.)
iterations6.sort()
print("The Confidence Interval is", iterations6[4999],",",iterations6[-4999])
'''
#6c
The Confidence Interval is 240605.07893808183 , 2245228.9573517917
'''

# (d) The investor's goal is to have a 65th-birthday balance of at least $300,000. What proportion of
# times was the investor successful?
x=0
for i in iterations6:
    if i >= 300000:
        x+=1
print(x/100000)
'''
#6d
The proportion of success was 0.89878
'''

# (e) Plot a histogram of balances from this simulation.
plt.hist(iterations6, bins=200, range=[0, 3500000]) 
'''
#6e
see attached.
'''


# In[253]:

# 7. Assume the savings pattern and rate of return until the 65th birthday given in question 5. After
# that, the investor adopts a more conservative investment strategy that produces an annual fixed rate
# of return mu = 3.5% continuous. Suppose the investor plans to make withdrawals of $25,000 on each
# birthday 66, 67, 68, ... 100. Find the balance on the investor's 100th birthday, immediately after the
# last withdrawal. Make a table of the birthdays from 65 to 100, and the balances.

balance7 = []
mu7 = .035

deposit=3000
Bi=50000

for i in range(40,65):  # same as 5 until age 65
    balance7.append(Bi)
    Bi = (np.exp(mu)*Bi) + deposit
    deposit = deposit*np.exp(.03)


for i in range(65,101): # when hit age 65, change to fixed rate with 3.5% and withdraw 25k
    balance7.append(Bi)
    Bi = (np.exp(.035)*Bi) - 25000
          
balance7 = np.round(balance7, 2)
len(balance7)

table7 = pd.DataFrame(columns={'Balance'}, index=(range(40,101)))
table7.index.name = 'Age'
table7['Balance']=balance7
print(table7)
'''
#7
       Balance
Age           
40    50000.00
41    56948.13
42    64536.26
43    72817.72
44    81850.12
45    91695.71
46   102421.74
47   114100.87
48   126811.61
49   140638.73
50   155673.82
51   172015.80
52   189771.51
53   209056.35
54   229994.92
55   252721.79
56   277382.29
57   304133.33
58   333144.36
59   364598.32
60   398692.74
61   435640.90
62   475673.06
63   519037.80
64   566003.51
65   616859.91
66   613832.28
67   610696.80
68   607449.64
69   604086.82
70   600604.22
71   596997.57
72   593262.45
73   589394.28
74   585388.34
75   581239.70
76   576943.29
77   572493.84
78   567885.90
79   563113.83
80   558171.78
81   553053.70
82   547753.31
83   542264.13
84   536579.42
85   530692.22
86   524595.32
87   518281.25
88   511742.28
89   504970.39
90   497957.29
91   490694.38
92   483172.78
93   475383.25
94   467316.26
95   458961.93
96   450310.02
97   441349.93
98   432070.69
99   422460.92
100  412508.86

'''


# In[ ]:

# 8. Assume the savings pattern and rate of return until the 65th birthday given in question 6. After that,
# the investor adopts a more conservative investment strategy that produces an annual rate of return has
# a lognormal distribution with mean mu = 3.5% and standard deviation mu = 5.1%. Suppose the investor
# plans to make withdrawals of $25,000 on each birthday 66, 67, 68, ... 100. Simulate 100,000 times
# the balance on the investor's 100th birthday, then use the results to answer the following questions
# regarding these balances:

# 6. Repeat question 4, but suppose that the birthday deposits start at $3000 on the 41st birthday, and
# increase by 3% continuous each year until the 65th birthday as in 5. Use the simulations to answer
# (a){(e).


# (a) What is the mean balance?

balance8 = []
mu8 = .035
sigma8 = .051


iterations8 = []
for x in range(1,100001):
    Bi=50000
    deposit=3000
    for i in range(40,65):  
        Bi = (np.exp(np.random.normal(mu2, sigma2, 1))*Bi)+deposit # same as in 6
        deposit = deposit*np.exp(.03)
    for i in range(65,101):
        Bi = (np.exp(np.random.normal(mu8, sigma8, 1))*Bi)-25000 # when hit age 65, change to fixed rate with 3.5% and withdraw 25k
    Bi=np.asscalar(Bi)
    iterations8.append(Bi)
iterations8

sampmu8 = np.round(np.mean(iterations8),2)
print("%.2f" % sampmu8)
'''
#8a
1213345.66
'''


sampmu8 = np.round(np.mean(iterations8),2)
print("%.2f" % sampmu8)

# (b) What is the median balance?
median8 = np.round(np.median(iterations8),2)
print("%.2f" % median8) 
'''
#8b
447045.21
'''

# (c) Give a 95% confidence interval for the balance. (That is, find the range of balances 
# that make up the middle 95% of simulated balances.)
iterations8.sort()
print("The Confidence Interval is", iterations8[4999],",",iterations8[-4999])
'''
#8c
The Confidence Interval is -1011329.6045328734 , 5989555.356568553
'''

# (d) The investor's goal is to have a 65th-birthday balance of at least $300,000. What proportion of
# times was the investor successful?
x=0
for i in iterations8:
    if i >= 0:
        x+=1
print(x/100000)
'''
#8d
The proportion of success was 0.62782.
.
'''

# (e) Plot a histogram of balances from this simulation.
plt.hist(iterations8, bins=200, range=[0, 3500000]) 
'''
#8e
see attached.
'''

